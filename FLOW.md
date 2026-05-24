# The flow of app usage

This document lays out the main flows of the app, and what it needs to do.

Note all URLs should be relative to the `BASE_URL` environment variable, which is `/` if not
defined.

Admins will authenticate at `/admin/login` before accessing any admin things.

## 0. (deployment) Admins set event name

The `EVENT_NAME` environment variable will be set to something like `"ScottyLabs TartanHacks 2027"`.

## 0.5. Admin gives Google access

There should be a special page `/config/authenticate`, blocked behind admin authentication,
which lets the user give the app Google permission to edit the drive and files within it.

## 1. Admins configure prizes

These will be managed via a page `/admin/prizes`.
They will include the name and the monetary value as a `Decimal`
(note: internal representation is not a `float` because we are working with money).

### Prize spreadsheet format

Prize details can be uploaded in bulk using a `.csv` of the form

| Prize name           | Prize amount |
|----------------------|--------------|
| Awesome prize        | 1000.00      |
| Awesomer prize       | 5000         |
| Oddly specific prize | 420.69       |

All units are assumed to be USD. `1000.00` is $1000 US dollars.
Prize amounts *may* get stripped up `$` characters if the implementers are feeling like handling
errors that day.

## 2. Admins add winner details

These will be input via a page `/admin/winners`, either manually or via a spreadsheet upload.
These will include an email and a list of the prizes won by that person.

### Spreadsheet format

There are two formats supported, because I'm not sure which will be easier.

#### Emails And Prizes

One `.csv` will be uploaded in the format.

| Recipient email                                             | Prize name              |
|-------------------------------------------------------------|-------------------------|
| khaled@djkhaled.com                                         | Grammy                  |
| fhcc@phys.cam.ac.uk, jdw@phys.cam.ac.uk, mauricew@kings.edu | Nobel Prize In Medicine |
| albert.einstein@ipi.ch                                      | Nobel Prize In Physics  |
| khaled@djkhaled.com                                         | "Another one"           |

The system will, with whatever degree of fuzzing the implementers feel like doing
but that should never result in incorrect matches, try to match prize name to prize id.
If it fails, it will error with a specific list of errors in the format.

| Unknown Prize Name     | Affected emails                          |
|------------------------|------------------------------------------|
| 2nd Place Jacket       | cdimarco@masters.com                     |
| Zeroeth place          | dolivaw@robts.com, greventlov@robots.com |
| Posthumous Nobel Prize | rosalindf@kings.edu                      |
| Fsirt place            | bob@hotmail.com, joe@yahoo.com           |

Prizes that do match should succeed.
To aid in the ease of working with this, if a duplicate is uploaded
(e.g. `twoods@masters.com` already won the Green Jacket prize, but is uploaded again as an entry),
it will only be reported as a duplicates count that was ignored and will not error.

Alternatively, the input table can instead have a "Prize ID" column.
If this column is included, it will be used instead of the name to match to the prizes.
If a prize ID does not exist, it will be reported in the same format.
If a "Prize name" column is included, it should not be used as a fallback.

#### Emails, Teams, And Prizes

Alternatively, two spreadsheets can be uploaded.

One maps emails to teams.

| Team name      | Member emails               |
|----------------|-----------------------------|
| RedBull Racing | pierre@rbr.com, max@rbr.com |
| Owl City       | adam.young@gmail.com        |
| RedBull Racing | alex@rbr.com                |

And the other maps teams to prizes. This should only allow 1-to-1 mappings, and no duplicates.

| Team name      | Prize name                 |
|----------------|----------------------------|
| RedBull Racing | Drivers' Championship      |
| Owl City       | Platinum                   |
| RedBull Racing | Constructors' Championship |

If a team is mapped to a prize but that team does not exist,
a warning is given for that specific one, other correct uploaded rows should succeed.
It is acceptable to have teams listed that do not win anything.
If an email has already been mapped to a prize, it is reported as a duplicate, but accepted, just
like previously.

Prize names that cannot be mapped are reported the same way as in
the [other format](#emails-and-prizes).

As above, the "Prize ID" column can be given, behaving the same way as in
the [other format](#emails-and-prizes).

## 3. Admins choose to send emails

This will send an individualized email to every email that won a prize
with a personalized link (`/form/{some-unique-id}`) to open a portal where the winner can enter
their details.

They should also be able to individually select people to send emails to,
and see a timestamp of when an email was last sent to a winner.

## 4. Winners fill out details

The link in their email takes them a form specifically for them.
Upon clicking[^1], it should, if not already created,

1. create the Google Drive folder
2. create the backing spreadsheet within it
3. share the folder with the person

It should load the data from the spreadsheet (never from the DB copy)[^2] to populate the form with
existing data
(that is the backing source if people need to come back to their responses).

Winners can save their changes, which will both store an immediate copy in the database
(to allow for faster saving and some level of resilience in case of Google Drive issues),
and queue work on a full sync to the backing Google Sheet.

[^1]: The reasoning behind waiting until now is that it serves as a way to verify the email is valid
before needing to share.

[^2]: Yes, it will be slow to load the page. No, I don't think it's worth adding complex cache
invalidation.
I suppose you could check the last updated time on the sheet, but honestly Google will send
you that timestamp and all the data in about the same amount of time.

## 5. Winners submit their details

The server fills the correct PDFs out for them and uploads them to the Drive folder.
Hopefully their forms get done faster and with fewer back-and-forths for errors.

## BONUS: 6. Winners update their forms where errors were made

I really hope this isn't needed. Let's not implement this functionality for now,
and only come back to it if it's determined we need it.

The form should continue syncing to the sheet in the same way, and create a new version of the
filled documents
(read: *update*[^3], NOT delete and recreate;
see [revisions docs](https://developers.google.com/workspace/drive/api/guides/manage-revisions) for
more).

[^3]: The fascination with this is because we can view old versions.
Since Google is willing to store everything forever (basically),
we never lose data due to a mistake. The sheet changes are tracked,
the document revisions are tracked, and it's all undoable if needed.