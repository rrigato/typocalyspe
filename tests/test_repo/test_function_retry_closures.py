import unittest
from typocalypse.repo.function_retry_closures import retry


class TestRetry(unittest.TestCase):

    def test_retry_succeeds_on_first_try(self):
        """
        GIVEN
            - The retry annotation is used
        WHEN
            - The function suceeds
        THEN
            - The function is called once
        """
        call_count = 0

        @retry(tries=3, delay=0.1)
        def successful_function():
            nonlocal call_count
            call_count += 1
            return "success"

        result = successful_function()
        self.assertEqual(result, "success")
        self.assertEqual(call_count, 1)

