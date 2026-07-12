# API Testing Using Postman

## Objective

This project demonstrates REST API testing using Postman and the JSONPlaceholder public API.

## Features Covered

* GET Request
* POST Request
* PUT Request
* DELETE Request
* Environment Variables
* Response Validation
* Status Code Validation
* JavaScript Test Scripts

## Environment Variables

* base_url
* user_id
* post_id

## Test Cases

### GET User

* Verify status code is 200
* Verify correct user ID
* Verify response contains required fields

### POST Create Post

* Verify status code is 201
* Verify response contains an ID
* Verify submitted data matches the response

### PUT Update Post

* Verify status code is 200
* Verify title, body, and userId are updated

### DELETE Post

* Verify successful deletion response (200 or 204)

## Tool Used

* Postman
* JSONPlaceholder API
