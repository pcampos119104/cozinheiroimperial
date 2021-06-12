from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains
assert_not_contains = _test_case.assertNotContains
assert_template_used = _test_case.assertTemplateUsed
assert_equals = _test_case.assertEquals
assert_true = _test_case.assertTrue
assert_false = _test_case.assertFalse
