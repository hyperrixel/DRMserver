# Constants

## Key Constants
- `KEY_ERROR`: Represents the key for error responses.
- `KEY_RESULT`: Represents the key for success responses.

## Enum-Like Constants

### EncryptionDepth
- `BIT_128`: Represents a 128-bit encryption depth.
- `BIT_256`: Represents a 256-bit encryption depth.

### EncryptionGenerator
- `RANDOM`: Represents a random encryption generator.
- `FIXED`: Represents a fixed encryption generator.
- `FROM_COLLECTION`: Represents an encryption generator from a collection.

### EncryptionType
- `AES_CBC`: Represents AES-CBC encryption type.
- `AES_CTR`: Represents AES-CTR encryption type.

### ProtectionType
- `CUSTOM`: Represents a custom protection type.
- `DRM_BASE`: Represents a DRM base protection type.
- `FAIR_PLAY`: Represents a Fair Play protection type.
- `PLAY_READY`: Represents a Play Ready protection type.
- `WIDEVINE`: Represents a Widevine protection type.

### Status
- `NON_EXISTING`: Represents a non-existing status.
- `DELETED`: Represents a deleted status.
- `SUSPENDED`: Represents a suspended status.
- `ACTIVE`: Represents an active status.

### StreamAccess
- `NOT_ACCESSIBLE`: Represents a stream that is not accessible.
- `OPEN`: Represents an open stream.
- `RESTRICTED_WITHOUT_SUBSCRIPTION`: Represents a restricted stream without subscription.
- `FREE_FOR_SUBSCRIBE`: Represents a free-for-subscribe stream.
- `RESTRICTED_WITH_SUBSCRIPTION`: Represents a restricted stream with subscription.

### StreamRestrictionBase
- `NO_RESTRICTION`: Represents no stream restriction.
- `TIME_BASED`: Represents a time-based stream restriction.
- `COUNT_BASED`: Represents a count-based stream restriction.
- `GEOLOCATION_BASED`: Represents a geolocation-based stream restriction.

### StreamType
- `DASH_CMAF`: Represents a DASH CMAF stream.
- `HLS`: Represents an HLS stream.
- `MULTIPART`: Represents a multipart stream.
- `RTMP`: Represents an RTMP stream.
- `RTSP`: Represents an RTSP stream.
- `SRT`: Represents an SRT stream.
- `WebRTC`: Represents a WebRTC stream.

# Mid-Level Classes

## AntMediaStream
- Represents an Ant Media Stream.
- Attributes: `name`, `status`, `stream_type`.

## StreamAccess
- Represents stream access information.
- No specific attributes defined.

## StreamStatistics
- Represents stream statistics.
- No specific attributes defined.

## UserCredentials
- Represents user credentials.
- No specific attributes defined.

## UserPaymentInformation
- Represents user payment information.
- No specific attributes defined.

## UserStatistics
- Represents user statistics.
- Attributes: `registered`, `streams_count`, `views_count`.

# Top-Level Classes

## Stream
- Represents a stream.
- Attributes: `name`, `ams_stream`, `status`, `statistics`, `access`.

## User
- Represents a user.
- Attributes: `user_id`, `status`, `credentials`, `payment`, `statistics`.

# Functions

## all_keys_set
- Checks if all specified keys are present in the given dictionary.

## const_exists
- Checks if a given key exists in a specified source.

## error_response
- Generates an error response with the provided text.

## get_result_template
- Returns a template for response results.

## success_response
- Generates a success response with the provided data.
