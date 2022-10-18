"""
Task: Count the smiley faces!
Given an array (arr)as an argument complete the function countSmileys
that should return the total number of smiling faces.

Rules for a smiling face:
 - Each smiley face must contain a valid pair of eyes - : or ;
- A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
- Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
"""


def count_smileys(arr):
    smiling_list = [":)", ":D", ";D", ";)", ":-)", ";-)", ":-D", ";-D", ":~D", ";~D", ":~)", ";~)"]
    smiling_faces = sum(face in smiling_list for face in arr)
    return smiling_faces


# Test
print(f"Expected res.: {4}. Current res.: {count_smileys([':D',':~)',';~D',':)'])}")
print(f"Expected res.: {2}. Current res.: {count_smileys([':)',':(',':D',':O',':;'])}")
