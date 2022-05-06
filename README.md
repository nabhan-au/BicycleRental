# Requirement
|Name  | Recommended version(s)|   
|------|-----------------------|
|Python | 3.8 or higher |

# Document
API Documentation: https://nabhan-au.github.io/BicycleRental/


# Install pacakage
1. create versual environment
    ```
    python -m venv venv
    ```
2. activate versual environment    
    - for Mac OS / Linux.   
    ```
    source venv/bin/activate
    ```
    - for Windows.   
    ```
    venv\Scripts\activate
    ```

3. Install requirement package
    ```
    pip install -r requirement.txt
    ```

4. Create database and table
    ```
    sqlite3 rental.db < rental.schema
    ```

5. Load data
    ```
    .mode csv
    .import data/bicycle.csv bicycle
    .import data/users.csv users
    ```
