import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

# ----------------- Trie Implementation -----------------

class TrieNode:
    def __init__(self, char=''):
        self.char = char
        self.children = {}    # Dictionary mapping characters to TrieNode.
        self.is_end = False   # Flag indicating end of a valid word.
        self.weight = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def delete(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                print(f"Word not found, cannot be deleted: {word}")
                return
            node = node.children[char]
        node.is_end = False

    def _autocomplete(self, node, prefix):
        suggestions = []
        if node.is_end:
            suggestions.append(prefix)
        for char, child in node.children.items():
            suggestions.extend(self._autocomplete(child, prefix + char))
        return suggestions

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._autocomplete(node, prefix)

def load_words_to_trie(filename):
    """Reads words from a file (one per line) and builds the trie."""
    trie = Trie()
    with open(filename, 'r', encoding="latin1") as file:
        for line in file:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie

# ----------------- PyQt5 GUI -----------------

class AutoCompleteGUI(QtWidgets.QWidget):
    def __init__(self, trie, parent=None):
        super().__init__(parent)
        self.trie = trie
        self.init_ui()

    def init_ui(self):
        # Create layout, line edit, and list widget.
        layout = QtWidgets.QVBoxLayout(self)
        self.input_box = QtWidgets.QLineEdit(self)
        self.input_box.setPlaceholderText("Type to search...")
        self.suggestion_list = QtWidgets.QListWidget(self)
        
        layout.addWidget(self.input_box)
        layout.addWidget(self.suggestion_list)

        # Connect text change signal to the autocomplete update method.
        self.input_box.textChanged.connect(self.update_suggestions)

        self.setWindowTitle("Trie Autocomplete Demo")
        self.resize(400, 300)

    def update_suggestions(self, text):
        # Clear current suggestions.
        self.suggestion_list.clear()
        if not text:
            return
        suggestions = self.trie.autocomplete(text)
        # Populate the list widget with suggestions.
        self.suggestion_list.addItems(suggestions)

def main():
    # Load trie from words.txt
    trie = load_words_to_trie("rockyou.txt")
    
    app = QtWidgets.QApplication(sys.argv)
    gui = AutoCompleteGUI(trie)
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
