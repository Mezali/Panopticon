db.createUser(
    {
        user: "Mazali",
        pwd: "@utec8415",
        roles: [
            {
                role: "readWrite",
                db: "banco"
            }
        ]
    }
)