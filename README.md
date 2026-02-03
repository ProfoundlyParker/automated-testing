# 💻 Magento Automated Testing Suite

This repository contains a comprehensive set of automated end-to-end tests for the [Magento Open Source Demo Site](https://magento.softwaretestingboard.com/), written in **Python** using **Selenium**, **pytest**, and **Geckodriver**.

These tests cover nearly all critical user workflows across desktop and mobile views, and are structured for easy maintenance and scalability.

**Note: As of 2/2/26, the Magento faux e-commerce testing site is no longer active. This project will be updated to reflect another live site soon.**

## ✅ Features & Test Coverage

### 🔐 Authentication Flows
- Create account (valid and duplicate emails)
- Login and logout
- Change password & email

### 👤 My Account
- Update/add billing/shipping addresses
- View past orders (with and without order history)

### 🛒 Cart & Checkout
- Add, update, and remove cart items
- Apply promo codes (valid and invalid)
- Test quantity limits (negative and large numbers)
- Checkout with single or multiple addresses

### 🎁 Wishlist Functionality
- Save item(s) to wishlist
- Move wishlist item to cart
- Delete wishlist item

### 🔍 Product Browsing
- Valid and invalid search queries
- Navigate to categories
- Filter products by size, color, and price
- Sort products by price and name
- Navigate through product image galleries
- Leave a product review

### 📱 Mobile View Test
- Navigate through mobile menu
