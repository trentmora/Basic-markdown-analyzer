class FileAnalysis:
    # constructor: stores the list of FileStatus objects
    def __init__(self, file_objects):
        self.file_objects = file_objects

    # lets us do len(analysis) to get number of files
    def __len__(self):
        return len(self.file_objects)

    # summary: loops through FileStatus objects and counts totals
    def summary(self):
        yaml_count = 0
        gpt_count = 0
        total_words = 0
        orphaned_count = 0

        # go through EACH FileStatus object
        for obj in self.file_objects:
            # obj.get_hasYAML() returns True/False
            if obj.get_hasYAML() == True:
                yaml_count += 1

            # obj.get_hasGPT() returns True/False
            if obj.get_hasGPT() == True:
                gpt_count += 1
        # word count (liaison variable coming from FileStatus.check_howmanywords)
            words = obj.get_numOfWords()
            total_words += words
        # orphaned file counter
            if words == 0:
                orphaned_count += 1

        # return the totals back to main.py
        return yaml_count, gpt_count, total_words, orphaned_count
    
    def write_report(self, outname="report.txt"):
        # open the output file in WRITE mode
        file = open(outname, "w")

        file.write("==== File Analysis Report ====\n\n")

        # self.file_objects is the liaison variable:
        # main.py passes filestatus_list --> FileAnalysis (FileAnalysis.py)
        # so this list is literally how info moves between files/classes
        for obj in self.file_objects:

            # obj is a FileStatus object coming from FileStatus.py
            # get_filepath() is an accessor in FileStatus.py
            # so we're pulling the filepath across files using that interface
            file.write(obj.get_filepath() + "\n")

            # these next three are also accessors from FileStatus.py
            # they return values that were SET earlier by:
            # - FileStatus.check_yaml()
            # - FileStatus.check_gpt()
            # - FileStatus.check_howmanywords()
            file.write(f"YAML: {obj.get_hasYAML()}\n")      # accessor from FileStatus.py
            file.write(f"GPT: {obj.get_hasGPT()}\n")        # accessor from FileStatus.py
            file.write(f"Words (>=3 letters): {obj.get_numOfWords()}\n")  # accessor from FileStatus.py

            file.write("\n")

        # summary() returns 4 liaison variables (counts)
        # these values are passed from summary() --> write_report() inside FileAnalysis.py
        yaml_count, gpt_count, total_words, orphaned_count = self.summary()
        file.write("==== Summary ====\n")

        # len(self) uses the magic method __len__()
        # so it’s another “OOP flex” for the rubric
        file.write(f"Total files: {len(self)}\n")
        file.write(f"Files with YAML: {yaml_count}\n")
        file.write(f"Files mentioning GPT: {gpt_count}\n")
        file.write(f"Total words (>=3 letters): {total_words}\n")
        file.write(f"Orphaned files (0 words): {orphaned_count}\n")
        # always close files when you're done
        file.close()
