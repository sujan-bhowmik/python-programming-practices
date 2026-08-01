"""
Example 04: PEP8 Naming Conventions and Comments
Goal: Demonstrate professional, PEP8-compliant naming and documentation.
NOTE: This triple-quoted string right here IS a module docstring, stored
automatically in the built-in __doc__ variable.
"""

VAT_RATE = 0.15  # 15% value added tax (CONSTANT: UPPER_CASE)

product_base_price = 1000
applied_discount = 0.10  # snake_case for variables: clear, descriptive

discounted_price = product_base_price - (product_base_price * applied_discount)
payable = discounted_price + (discounted_price * VAT_RATE)

print(f"Base price           : {product_base_price}")
print(f"Discount applied      : {applied_discount * 100:.0f}%")
print(f"Final payable (w/ VAT): {payable:.2f}")

# Read this file's own module docstring at runtime.
print(__doc__)
