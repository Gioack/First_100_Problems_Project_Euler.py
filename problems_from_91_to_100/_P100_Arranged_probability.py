def arranged_probability():
    # We want to solve this:
    # (blue_disks/total)*((blue_disks-1)/(total-1)) = 1/2)
    # The following just uses some formulae to solve the equation:
    blue_disks = 15
    total = 21
    while total < 1000000000000:
        potential_blue_disks = 3*blue_disks + 2*total - 2
        potential_total = (4*blue_disks) + (3*total) - 3
        blue_disks, total = potential_blue_disks, potential_total
    return blue_disks


print(arranged_probability())
