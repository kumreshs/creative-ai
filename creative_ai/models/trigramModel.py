from creative_ai.utils.print_helpers import ppGramJson

class TrigramModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.
                  This function is done for you.
        """

        return ppGramJson(self.nGramCounts)

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a three-dimensional dictionary. For
                  examples and pictures of the TrigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries as values,
                  where those inner dictionaries have strings as keys
                  and dictionaries of {string: integer} pairs as values.
        """
        data = text

        for line in data:
            for word1, word2, word3 in zip(line, line[1:], line[2:]):
                try:
                    self.nGramCounts[word1][word2][word3] += 1
                except:
                    try:
                        self.nGramCounts[word1][word2].update({word3: 1})
                    except:
                        try:
                            self.nGramCounts[word1].update({word2: {word3: 1}})
                        except:
                            self.nGramCounts[word1] = {word2: {word3: 1}}

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the TrigramModel, see the spec.
        """

        if len(sentence) < 2:
            return False

        word1 = sentence[-2]
        word2 = sentence[-1]

        if word1 in self.nGramCounts:
            if word2 in self.nGramCounts[word1]:
                return True

        return False

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  TrigramModel sees as candidates, see the spec.
        """
        word1 = sentence[-2]
        word2 = sentence[-1]

        if word1 in self.nGramCounts:
            if word2 in self.nGramCounts[word1]:
                return self.nGramCounts[word1][word2]



        return {}


###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # An example trainModel test case
    uni = TrigramModel()

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    uni.trainModel(text)
    # Should print: { 'brown': 2, 'dog': 1, 'fox': 1, 'lazy': 1, 'the': 2 }
    print(uni)
