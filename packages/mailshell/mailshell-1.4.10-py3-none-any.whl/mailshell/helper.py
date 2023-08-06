import subprocess

VERSION = subprocess.getoutput("pip freeze | grep mailshell").split("==")[1]
DESCRIPTION = "send and check emails faster from the terminal"
COPYRIGHT = "Copyright (c) 2022 Malki Abderrahman"
EPILOG = "project home page on https://github.com/malkiAbdoo/mailshell"
USAGE = "msl [OPTION] | [COMMAND] [file]. See 'msl --help'."
IMAP_CRITERIAS = r"""
Search commands:

- FLAGGED
Messages with the \Flagged flag set.

- FROM 'string'
Messages that contain the specified string in the envelope structure's FROM field.

- HEADER 'field-name' 'string'
Messages that have a header with the specified field-name (as defined in [RFC-823]) and that contains the specified string in the [RFC-822] field-body.

- KEYWORD 'flag'
Messages with the specified keyword set.

- LARGER 'n'
Messages with an RFC821.SIZE larger than the specified number of octets.

- NEW
Messages that have the \Recent flag set but not the \Seen flag. This is functionally equivalent to "(RECENT UNSEEN)".

- NOT 'search-key'
Messages that do not match the specified search key.

- OLD
Messages that do not have the \Recent flag set. This is functionally equivalent to "NOT RECENT" (as opposed to "NOT NEW").

- ON 'date'
Messages whose internal date is within the specified date.

- OR 'search-key0' 'search-key2'
Messages that match either search key.

- RECENT
Messages that have the \Recent flag set.

- SEEN
Messages that have the \Seen flag set.

- SENTBEFORE 'date'
Messages whose [RFC-823] Date: header is earlier than the specified date.

- SENTON 'date'
Messages whose [RFC-823] Date: header is within the specified date.

- SENTSINCE 'date'
Messages whose [RFC-823] Date: header is within or later than the specified date.

- SINCE 'date'
Messages whose internal date is within or later than the specified date.

- SMALLER 'n'
Messages with an RFC821.SIZE smaller than the specified number of octets.

- SUBJECT 'string'
Messages that contain the specified string in the envelope structure's SUBJECT field.

- TEXT 'string'
Messages that contain the specified string in the header or body of the message.

- TO 'string'
Messages that contain the specified string in the envelope structure's TO field.

- UID 'message set'
Messages with unique identifiers corresponding to the specified unique identifier set.

- UNANSWERED
Messages that do not have the \Answered flag set.

- UNDELETED
Messages that do not have the \Deleted flag set.

- UNDRAFT
Messages that do not have the \Draft flag set.

- UNFLAGGED
Messages that do not have the \Flagged flag set.

- UNKEYWORD 'flag'
Messages that do not have the specified keyword set.

- UNSEEN
Messages that do not have the \Seen flag set.
"""

