from PySide2.QtCore import QAbstractListModel, Qt, Signal, Slot, QModelIndex

class PersonModel(QAbstractListModel):

    NameRole = Qt.UserRole + 1
    AgeRole = Qt.UserRole + 2

    personChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.persons = [
            {'name': 'jon', 'age': 20},
            {'name': 'jane', 'age': 25}
        ]

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        if role == PersonModel.NameRole:
            return self.persons[row]["name"]
        if role == PersonModel.AgeRole:
            return self.persons[row]["age"]

    def rowCount(self, parent=QModelIndex()):
        return len(self.persons)

    def roleNames(self):
        return {
            PersonModel.NameRole: b'name',
            PersonModel.AgeRole: b'age'
        }

    @Slot(str, int)
    def addPerson(self, name, age):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.persons.append({'name': name, 'age': age})
        self.endInsertRows()

    @Slot(int, str, int)
    def editPerson(self, row, name, age):
        ix = self.index(row, 0)
        self.persons[row] = {'name': name, 'age': age}
        self.dataChanged.emit(ix, ix, self.roleNames())

    @Slot(int)
    def deletePerson(self, row):
        self.beginRemoveColumns(QModelIndex(), row, row)
        del self.persons[row]
        self.endRemoveRows()
