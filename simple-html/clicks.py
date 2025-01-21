# Click counter implementation
click_count = 0

def increment_click():
    """Increments and returns the global click count.
    
    Returns:
        int: Updated click count after incrementing
    """
    global click_count
    click_count += 1
    return click_count

for i in range(10):
    increment_click()

print(click_count)
click_count = 0
print(click_count)