import pytest
from examplepackagefb1258 import wisdom

class Tests:

  #
  # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
  #

  @pytest.fixture
  def example_fixture(self):
    '''
    An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
    '''

    # place any setup you want to do before any test function that uses this fixture is run

    yield # at th=e yield point, the test function will run and do its business

    # place with any teardown you want to do after any test function that uses this fixture has completed


  #
  # Test functions
  #

  def test_sanity_check(self, example_fixture):
    """
    Test debugging... making sure that we can run a simple test that always passes.
    Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
    From the main project directory, run the `python3 -m pytest` command to run all tests.
    """
    expected = True # the value we expect to be present
    actual = True # the value we see in reality
    assert actual == expected, "Expected True to be equal to True!"

  def test_get(self):
    """
    Verify get() function and make sure it returns a non-empty string.
    Note that for example purposes, we have not used the example_fixture in this test functino.
    """
    # since get returns a random string, run it a bunch of times and verify the output
    for i in range(100):
      actual = wisdom.get()
      assert isinstance(actual, str), f"Expected get() to return a string. Instead, it returned {actual}"
      assert len(actual) > 0, f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"

  def test_content(self):
    """
    Make sure that the text returned by the get() function is actually from the correct poem.
    """
    # the full text of the actual Jabberwocky poem by Lewis Carroll
    full_text = '''Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

"Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!"

He took his vorpal sword in hand:
Long time the manxome foe he sought—
So rested he by the Tumtum tree,
And stood awhile in thought.

And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!

One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.

"And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!"
He chortled in his joy.

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.'''

    # since get returns a random string, run it a bunch of times and verify the output
    for i in range(100):
      actual = wisdom.get()
      assert actual in full_text, f"Expected the text returned by get() to be from the Jabberwocky poem by Lewis Carroll.  Instead, it returned '{actual}'."
