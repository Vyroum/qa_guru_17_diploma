login_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "login": {
            "type": "string"
        },
        "fam_inner": {
            "type": "string"
        },
        "phone_inner": {
            "type": "string"
        },
        "phone_inner2": {
            "type": "null"
        },
        "email_inner": {
            "type": "string"
        },
        "bonuses": {
            "type": "null"
        },
        "activ": {
            "type": "integer"
        },
        "confirm_email": {
            "type": "integer"
        },
        "confirm_phone": {
            "type": "integer"
        },
        "normalphone": {
            "type": "string"
        },
        "normalphone2": {
            "type": "null"
        },
        "nickname": {
            "type": "string"
        },
        "avatar_id": {
            "type": "integer"
        },
        "background_id": {
            "type": "null"
        },
        "needs_manager_confirmation": {
            "type": "integer"
        },
        "verified": {
            "type": "integer"
        },
        "avatar_achievement": {
            "type": "null"
        },
        "custom_avatar": {
            "type": "null"
        },
        "is_review_notification_enabled": {
            "type": "boolean"
        },
        "notification_settings": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "key",
                        "active",
                        "title"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "key",
                        "active",
                        "title"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "key",
                        "active",
                        "title"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "key",
                        "active",
                        "title"
                    ]
                },
                {
                    "type": "object",
                    "properties": {
                        "key": {
                            "type": "string"
                        },
                        "active": {
                            "type": "boolean"
                        },
                        "title": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "key",
                        "active",
                        "title"
                    ]
                }
            ]
        },
        "compare_goods": {
            "type": "array",
            "items": {}
        },
        "wishlists_goods": {
            "type": "array",
            "items": [
                {
                    "type": "integer"
                }
            ]
        },
        "business": {
            "type": "object",
            "properties": {
                "level": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "ord": {
                            "type": "integer"
                        },
                        "required_balance": {
                            "type": "integer"
                        },
                        "bonus_percentage": {
                            "type": "number"
                        },
                        "clients_count": {
                            "type": "integer"
                        },
                        "offers_count": {
                            "type": "integer"
                        },
                        "offers_total": {
                            "type": "integer"
                        },
                        "offers_average": {
                            "type": "integer"
                        },
                        "bonuses": {
                            "type": "integer"
                        },
                        "photo": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "integer"
                                        },
                                        "src": {
                                            "type": "string"
                                        },
                                        "full_src": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "name",
                                        "src",
                                        "full_src"
                                    ]
                                }
                            ]
                        },
                        "bonus_percentage_percent": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "description",
                        "ord",
                        "required_balance",
                        "bonus_percentage",
                        "clients_count",
                        "offers_count",
                        "offers_total",
                        "offers_average",
                        "bonuses",
                        "photo",
                        "bonus_percentage_percent"
                    ]
                },
                "nextLevel": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "ord": {
                            "type": "integer"
                        },
                        "required_balance": {
                            "type": "integer"
                        },
                        "bonus_percentage": {
                            "type": "number"
                        },
                        "clients_count": {
                            "type": "integer"
                        },
                        "offers_count": {
                            "type": "integer"
                        },
                        "offers_total": {
                            "type": "integer"
                        },
                        "offers_average": {
                            "type": "integer"
                        },
                        "bonuses": {
                            "type": "integer"
                        },
                        "photo": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "integer"
                                        },
                                        "src": {
                                            "type": "string"
                                        },
                                        "full_src": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "name",
                                        "src",
                                        "full_src"
                                    ]
                                }
                            ]
                        },
                        "bonus_percentage_percent": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "description",
                        "ord",
                        "required_balance",
                        "bonus_percentage",
                        "clients_count",
                        "offers_count",
                        "offers_total",
                        "offers_average",
                        "bonuses",
                        "photo",
                        "bonus_percentage_percent"
                    ]
                },
                "nextMoney": {
                    "type": "integer"
                },
                "progress": {
                    "type": "integer"
                }
            },
            "required": [
                "level",
                "nextLevel",
                "nextMoney",
                "progress"
            ]
        },
        "basket": {
            "type": "null"
        }
    },
    "required": [
        "id",
        "login",
        "fam_inner",
        "phone_inner",
        "phone_inner2",
        "email_inner",
        "bonuses",
        "activ",
        "confirm_email",
        "confirm_phone",
        "normalphone",
        "normalphone2",
        "nickname",
        "avatar_id",
        "background_id",
        "needs_manager_confirmation",
        "verified",
        "avatar_achievement",
        "custom_avatar",
        "is_review_notification_enabled",
        "notification_settings",
        "compare_goods",
        "wishlists_goods",
        "business",
        "basket"
    ]
}

add_to_cart = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "client_id": {
            "type": "null"
        },
        "active": {
            "type": "integer"
        },
        "id": {
            "type": "string"
        },
        "goods": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "basket_id": {
                            "type": "integer"
                        },
                        "good_id": {
                            "type": "integer"
                        },
                        "good_count": {
                            "type": "integer"
                        },
                        "brief": {
                            "type": "string"
                        },
                        "photos": {
                            "type": "object",
                            "properties": {
                                "urls": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "string"
                                        }
                                    ]
                                }
                            },
                            "required": [
                                "urls"
                            ]
                        },
                        "price": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "full_title": {
                            "type": "string"
                        },
                        "show_flag": {
                            "type": "integer"
                        },
                        "badges": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                            "type": "string"
                                        },
                                        "order": {
                                            "type": "integer"
                                        },
                                        "background_color": {
                                            "type": "string"
                                        },
                                        "text_color": {
                                            "type": "string"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "text",
                                        "order",
                                        "background_color",
                                        "text_color",
                                        "title",
                                        "type"
                                    ]
                                }
                            ]
                        },
                        "admin_link": {
                            "type": "string"
                        },
                        "price_old": {
                            "type": "null"
                        },
                        "markdown": {
                            "type": "boolean"
                        },
                        "seo_url": {
                            "type": "string"
                        },
                        "vendor": {
                            "type": "string"
                        },
                        "category_array": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "seo_url": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "seo_url"
                                    ]
                                },
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "seo_url": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "seo_url"
                                    ]
                                }
                            ]
                        },
                        "external_marketplace": {
                            "type": "boolean"
                        },
                        "similar": {
                            "type": "null"
                        },
                        "disable_delivery": {
                            "type": "boolean"
                        },
                        "bonus": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "id",
                        "basket_id",
                        "good_id",
                        "good_count",
                        "brief",
                        "photos",
                        "price",
                        "title",
                        "full_title",
                        "show_flag",
                        "badges",
                        "admin_link",
                        "price_old",
                        "markdown",
                        "seo_url",
                        "vendor",
                        "category_array",
                        "external_marketplace",
                        "similar",
                        "disable_delivery",
                        "bonus"
                    ]
                }
            ]
        }
    },
    "required": [
        "client_id",
        "active",
        "id",
        "goods"
    ]
}

cart_clear = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        }
    },
    "required": [
        "message"
    ]
}
