# Notes on UWS implementation

- Misc:
  - It is atypical that most of the success responses are 3xx redirects. This is flagged as an error by the redocly validator. I have set this to a warning for now. Additionally, there is inconsistency between individual endpoints / operations. Deleting a job returns a 200, and the job list, but other operations return 3xx redirects?