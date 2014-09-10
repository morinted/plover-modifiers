import copy

def makeDictionary(hotkeys, modifiers):

    dictionary_entries = []

    if len(modifiers) == 1:
        modifier = modifiers[0]
        for hotkey in hotkeys:
            dictionary_entries.append([modifier[0] + "/" + hotkey[0],
                modifier[1] + "(" + hotkey[1] + ")"])
    else:
        for modifier in modifiers:
            new_mods = list(modifiers)
            new_mods.remove(modifier)
            new_dict = makeDictionary(hotkeys, new_mods)
            dictionary_entries.extend(new_dict)
            iter_dict = copy.deepcopy(new_dict)
            for entry in iter_dict:
                dictionary_entries.append([modifier[0] + "/" + entry[0],
                    modifier[1] + "(" + entry[1] + ")"])
    return dictionary_entries           

def wrapDictionary(dictionary_entries):
    for entry in dictionary_entries:
        entry[0] = '"' + entry[0] + '"'
        entry[1] = '"{#' + entry[1] + '}"'
    return dictionary_entries

def writeDictionary(dictionary_entries, specials):
    modifiers_json = open('modifiers.json', 'w')
    modifiers_json.write("%s\n" % "{")
    for entry in dictionary_entries:
        modifiers_json.write("%s\n" % (entry[0] + ": " + entry[1] + ','))
    
    for special in specials:
        modifiers_json.write("%s\n" % special)

    modifiers_json.write("%s\n" % "}")

def makeEsses():
    esses = '"S'
    for i in range(99):
        esses += "/S"
    esses += '": "This entry allows the Plover buffer to increase to 100."'
    return esses

def neutralizeModifiers(modifiers):
    neutralized = []
    for modifier in modifiers:
        neutralized.append('"' + modifier[0] + '": "{}",')
    return neutralized

def main():

    # These are the keys to be pressed with modifiers.
    # If you'd like to add your own, use anything from the
    # "Available Key Names" table from this page:
    # https://sites.google.com/site/ploverdoc/appendix-the-dictionary-format

    hotkeys = [
        ["A*", "a"],    ["PW*", "b"],   ["KR*", "c"],   ["TK*", "d"],
        ["E*", "e"],    ["TP*", "f"],   ["TKPW*", "g"], ["H*", "h"],
        ["EU*", "i"],   ["SKWR*", "j"], ["K*", "k"],    ["HR*", "l"],
        ["PH*", "m"],   ["TPH*", "n"],  ["O*", "o"],    ["P*", "p"],
        ["KW*", "q"],   ["R*", "r"],    ["S*", "s"],    ["T*", "t"],
        ["U*", "u"],    ["SR*", "v"],   ["W*", "w"],    ["KP*", "x"],
        ["KWR*", "y"],  ["STKPW*", "z"],["S#", "1"],    ["T#", "2"],
        ["P#", "3"],    ["H#", "4"],    ["A#", "5"],    ["O#", "0"],
        ["#F", "6"],    ["#P", "7"],    ["#L", "8"],    ["#T", "9"],
        ["TKHRAO*ET", "Delete"],        ["SP*S", ""],   ["R-R", "Enter"],
        ["PW*FP", "BackSpace"],         ["STPH-P", "Up"],["STPH-G", "Down"],
        ["STPH-R", "Left"],             ["STPH-B", "Right"]
        ]

    # format of a Plover command: {#FirstMod(SecondMod(x))}
    # Where x is the hot key to hit

    modifiers = [
        ["KHR*", "Control_L"],  # Ctrl      (Kl)
        ["KPH*", "Super_L"],    # Command   (Km)
        ["THRA*", "Alt_L"],     # Alt       (Tla)
        ["STP*", "Shift_L"]     # Shift     (Sf)
        ]



    # Delete key is added
    # 100 esses is added - note it has no trailing comma!
    specials = []
    specials.extend(neutralizeModifiers(modifiers))
    specials.extend(['"TKHRAO*ET": "{#Delete}",',
                makeEsses()])

    dictionary_entries = makeDictionary(hotkeys, modifiers)
    dictionary_entries = wrapDictionary(dictionary_entries)
    writeDictionary(dictionary_entries, specials)
    print("All done, " +
        "'modifiers.json' should be available in the current directory.")

if __name__ == '__main__':
    main()