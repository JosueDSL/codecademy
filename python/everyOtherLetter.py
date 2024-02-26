if __name__ == "__main__":
    def every_other(string):
        string_list = ""
        for i ,char in enumerate(string):
            if i % 2 == 0:
                string_list += char
            else:
                continue
        return string_list
    
    print(every_other("hola wey"))
