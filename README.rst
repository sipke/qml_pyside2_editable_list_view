Pyside2 and QML example
=======================
Editable ListView from PySide using Python Thread
-------------------------------------------------

This is a port of Stack Overflow post `Editable qml/pyside2 listview`_ from PyQt5 to PySide2


Adding or removing from the UI works nicely and the ListView updates.

Doing the same from a timer using python Threading does not, as demonstrated by the update function in main.py (when queue variable is False).

The stack overflow site `SO Qt Queued Connection`_ and associated `Gist Qt Queued Connection`_ explain that QueuedConnections are necessary.

To compare between the two methods, change the variable queued between True or False at the start of the main.py script.

.. code:: python

    queued = False  # Change between False and True to test direct (which does not auto update) or queued signal (which does)

The Link class and the associated signal emit call are the key behind successful update of the UI from a thread.

.. code:: python

    link = Link()
    link.updateSignal.connect(ui.model.addPerson, Qt.QueuedConnection)  # This line ...
    ...
            link.updateSignal.emit("queued", age)  # ... and this line are the key

Stack Overflow Links

- https://stackoverflow.com/questions/46814961
- https://stackoverflow.com/questions/48793100

Associated Authors

- https://stackoverflow.com/users/7236880/eugeneoei
- https://stackoverflow.com/users/6622587/eyllanesc

Gist Links

- https://gist.github.com/eyllanesc/b257c9f784d16849dbaaf4e5bdcfd549

.. _Editable qml/pyside2 listview: https://stackoverflow.com/questions/46814961/how-to-insert-edit-qabstractlistmodel-in-python-and-qml-updates-automatically
.. _SO Qt Queued Connection: https://stackoverflow.com/questions/48793100/how-to-update-qml-listview-from-a-python-thread
.. _Gist Qt Queued Connection: https://gist.github.com/eyllanesc/b257c9f784d16849dbaaf4e5bdcfd549
