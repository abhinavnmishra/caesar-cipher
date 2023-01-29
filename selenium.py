from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox browser instance
driver = webdriver.Firefox()

# navigate to the webpage
driver.get("http://localhost/encryption.php")

# Encryption Test
string_input = driver.find_element_by_name("string")
string_input.send_keys("Hello World")
encryption_key = driver.find_element_by_name("encryption_key")
encryption_key.send_keys("secretkey")
encrypt_button = driver.find_element_by_name("encrypt")
encrypt_button.click()

# check for the expected encrypted string
encrypted_string = driver.find_element_by_xpath("//*[contains(text(), 'Encrypted String:')]")
assert encrypted_string.text == "Encrypted String: <expected_encrypted_string>"

# Decryption Test
encrypted_string_input = driver.find_element_by_name("encrypted_string")
encrypted_string_input.send_keys("<expected_encrypted_string>")
decryption_key = driver.find_element_by_name("decryption_key")
decryption_key.send_keys("secretkey")
decrypt_button = driver.find_element_by_name("decrypt")
decrypt_button.click()

# check for the expected decrypted
