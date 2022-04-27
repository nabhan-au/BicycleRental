# Requirement
|Name  | Recommended version(s)|   
|------|-----------------------|
|Python | 3.8 or higher |

# Document
UML Diagram/Package Diagram: https://lucid.app/lucidchart/78e46e32-1f4f-4dd8-847c-47f97fafd853/edit?invitationId=inv_2feebb46-6a69-40f7-a9be-bf3cc6a4767b


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
