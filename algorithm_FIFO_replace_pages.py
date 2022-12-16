class algorithm_FIFO:

    def __init__(self):
        """Initialize class"""

    def replace_pages_FIFO(self, pages, frames):
        """Return amount of missing pages for every data file"""

        missing_pages = 0
        operational_frame = []

        for page in pages:

            if page not in operational_frame:
                missing_pages = missing_pages + 1

                if len(operational_frame) < frames:
                    operational_frame.append(page)

                else:
                    operational_frame.pop(0)
                    operational_frame.append(page)

        return missing_pages

    def read_data_from_file(self, file_number):
        """Read data from data file"""

        list_of_pages = []

        with open(f"data/{file_number}.txt", "r") as f:
            for number in f.readlines():
                list_of_pages.append(number.strip())
            list_of_pages = [int(x) for x in list_of_pages]
            f.close()

            return list_of_pages

    def save_to_result_file(self):
        """Save results of algorithms to result file"""

        available_frames = [3, 5, 7]
        for frame in available_frames:
            with open(f"FIFO_results/{frame}.txt", "w") as f:
                for number in range(1, 51):
                    f.write(f"{self.replace_pages_FIFO(self.read_data_from_file(number), frame)}\n")
                f.close()
