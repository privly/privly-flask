.. _API:

PyVly API
*********

CSRF Protection
===============

Sessions
========

Cookie Based Sessions
=====================

Token Based Sessions
====================

Posts
=====

Creating New Content
--------------------

Create a post.

POST /posts

**Parameters**

**post[content]** - string - Optional

* Values: Any Markdown formatted string. No images supported.
* Default: None

The content is rendered on the website, or for injection into web pages.

**post[structured_content]** - JSON - Optional

* Values: Any JSON document
* Default: None

Structured content is for the storage of serialized JSON in the database.

**post[privly\_application]** - string - Optional

* Values: Any of the currently supported Privly application identifiers can be set here. Current examples include "PlainPost" and "ZeroBin", but no validation is performed on the string. It is only used to generate URLs into the static folder of the server.
* Default: None

**post[public]** - boolean - Optional

* Values: true, false
* Default: None

A public post is viewable by any user.

**post[random\_token]** - string - Optional

* Values: Any string
* Default: A random sequence of Base64 characters

The random token is used to permission requests to content
not owned by the requesting user. It ensures the user has access to the link, and not didn't crawl the resource identifiers.

**post[seconds\_until\_burn]** - integer - Optional

* Values: 1 to 99999999
* Default: None

The number of seconds until the post is destroyed.

If this parameter is specified, then the burn\_after\_date
is ignored.

**post[burn\_after\_date]** - DateTime - Required

* Value: "%Y-%m-%dT%H:%M:%SZ"
* Example: "2014-02-08T13:37:00Z"
* Default: 30 days from the current date

If this parameter is not specified, the server will generate a date.

Time is stored and delivered in UTC.

The day after which the content will be destroyed. The combined day,
month, and year must be within the next 14 days for users with
posting permission, or 2 days for users without posting permission.


**Response Headers**

* X-Privly-Url The URL for this content which should be posted to other
websites.


Viewing Content
---------------

Shows an individual post. The "owning user" is the user who created the original content behind the link. The owning user will be the only one with access to metadata for the post.

GET: /posts/:id

Example:

    {"created_at":"2012-09-05T04:08:31Z", // when the content was created (owning user only)
     "burn_after_date":"2012-09-19T04:08:31Z", // when the content will be destroyed
     "public":false, // whether everyone has read permission
     "updated_at":"2012-09-05T04:08:31Z", // when the content was updated (owning user only)
     "structured_content":{ // the content serialized by and for the privly-application
       "salt":"ytyzBr2OkEc",
       "iv":"RSBeCnAklAbi0qvq/P8twA",
       "ct":"23hqJJ7QKNkxpLVtfp9uEg"},
     "id":149, //the unique id of the content
     "user_id":2, //the id of the creating user. (owning user only)
     "content":null, // public cleartext content. this may be deprecated
     "random_token":"a53642b006", //see below
     "permissions":{ //current user's permissions on contents
       canshow: true,
       canupdate: false,
       candestroy: false,
       canshare: false}
    }

**Parameters**

**random_token** - string - Required

* Values: Any string of non-whitespace characters
* Default: None

Either the user owns the post, or they must supply this parameter.
Without this parameter, even with complete share access to the content,
the user will not be able to access this content.

**Response Headers**

* X-Privly-Url The URL for this content which should be posted to other
websites.


Updating Content
----------------

Update a post. Requires update permission or content ownership.

PUT /posts/:id
PUT /posts/:id

**id** - integer - Required

* Values: 0 to 9999999
* Default: None

The identifier of the post.

**random\_token** - string - Required

* Values: Any string of non-whitespace characters
* Default: None

Either the user owns the post, or they must supply this parameter.
Without this parameter, even with complete share access to the content,
the user will not be able to access this endpoint.

**post[content]** - string - Optional

* Values: Any Markdown formatted string. No images supported.
* Default: None

The content is rendered on the website, or for injection into web pages.

**post [structured\_content]** - JSON - Optional

* Values: Any JSON document
* Default: None

Structured content is for the storage of serialized JSON in the database.

**post[public]** - boolean - Optional

* Values: true, false
* Default: None

A public post is viewable by any user.

**post [random\_token]** - string - Optional

* Values: Any string
* Default: A random sequence of Base64 characters
The random token is used to permission requests to content
not owned by the requesting user. It ensures the user has access to the link,
and not didn't crawl the resource identifiers.

**post [seconds\_until\_burn]** - integer - Optional

* Values: 1 to 99999999
* Default: None

The number of seconds until the post is destroyed.
If this parameter is specified, then the burn\_after\_date
is ignored. Requires destroy permission.


**post [burn\_after\_date(1i)]** - integer - optional

* Values: 2012
* Default: 2012

The year in which the content will be destroyed
Requires destroy permission.

**post [burn\_after\_date(2i)]** - integer - optional

* Values: 1 to 12
* Default: current month

The month in which the content will be destroyed
Requires destroy permission.

**post [burn\_after\_date(3i)]** - integer - optional

* Values: 1 to 31

Default: Defaults to thirty days from now.

**Response Headers**

* X-Privly-Url The URL for this content which should be posted to other
websites.


Destroying Content
------------------

Destroy a post. Requires destroy permission, or content ownership.

DELETE /posts/:id
DELETE /posts/:id

**Parameters**

**id** - integer - Required

* Values: 0 to 9999999
* Default: None

The identifier of the post.

**random\_token** - string - Required

* Values: Any string of non-whitespace characters
* Default: None

Either the user owns the post, or they must supply this parameter.
Without this parameter, even with complete share access to the content,
the user will not be able to access this endpoint.





