def _getUserInfoColumnIds(data, usernameColName: str, passwordColName: str):
    return data.columns.get_loc(usernameColName), data.columns.get_loc(passwordColName)

def getListAccount(data, usrColName: str, pwdColName: str):
    usernameColId, passwordColId = _getUserInfoColumnIds(data, usrColName, pwdColName)
    data = data.to_numpy()
    listAccount = []
    for i in range(1, len(data)):
        newAccount = {
            "username": data[i][usernameColId],
            "password": data[i][passwordColId]
        }
        listAccount.append(newAccount)
    return listAccount