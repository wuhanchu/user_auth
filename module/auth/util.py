def generate_token_cache_key(token_string):
    """当前token的缓存KEY

    Args:
        key (_type_): _description_

    Returns:
        _type_: _description_
    """
    token_cache_key = f"user_auth:token:{token_string}"
    return token_cache_key
