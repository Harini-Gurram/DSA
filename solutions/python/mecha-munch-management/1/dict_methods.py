"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item]=current_cart.setdefault(item,0)+1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    cart=dict.fromkeys(notes,1)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    for item in recipe_updates:
        ideas[item[0]]=item[1]
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_items=dict(sorted(cart.items()))
    return sorted_items
    


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    for item in cart:
        aisle_map=aisle_mapping[item]
        aisle_map.insert(0,cart[item])
        cart[item]=aisle_map
    sorted_items=dict(sorted(cart.items(),reverse=True))
    return sorted_items


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for item in fulfillment_cart:
        count=store_inventory[item][0]-fulfillment_cart[item][0]
        if count==0:
            new_item=['Out of Stock']+store_inventory[item][1:]
            store_inventory[item]=new_item
        else:
            new_item=[count]+store_inventory[item][1:]
            store_inventory[item]=new_item
    return store_inventory
