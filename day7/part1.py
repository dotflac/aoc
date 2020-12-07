def find_all_outer_bags(inner_bag, ruleset):
    outer_bags = set()
    for k, v in ruleset.items():
        if inner_bag in v and k not in outer_bags:
            outer_bags.add(k)
            outer_bags.update(find_all_outer_bags(k, ruleset))
    return outer_bags
    
if __name__ == '__main__':
    rules = {}
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip('.\n').replace('bags','bag')
            outer, inner = line.split(' contain ')
            rules[outer] = inner
    print(len(find_all_outer_bags('shiny gold bag', rules)))
    


            
    