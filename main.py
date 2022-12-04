from components import imageCompressor as iC, mainFunctions as mF, localColors as Color
import concurrent.futures
import argparse
import time
import os

# measuring number of cores in your machine. Will utilize all of them. you can set cores manually such as n_cores = 4
n_cores = os.cpu_count()

if __name__ == '__main__':

    # passing commands to out to command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=str, required=True)
    parser.add_argument('-d', type=str, required=True)
    parser.add_argument('-f', type=str, required=True)
    parser.add_argument('-w', type=int, required=True)
    parser.add_argument('-q', type=int, required=True)
    args = parser.parse_args()

    # begging of time measure
    time_start = time.time()

    # building list of files from generator function
    image_list = [file for file in mF.build_file_list(args.l)]

    # starting multicore loop with editing output
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_cores) as executor:
        # Start the load operations and mark each future with its URL
        future_to_image = {executor.submit(mF.start_command, image, args.l, args.d, dformat=args.f, max_width=args.w,
                                           quality=args.q): image
                           for image in image_list}

        # returning output from pool
        for future in concurrent.futures.as_completed(future_to_image):
            image = future_to_image[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (image, exc))
            else:
                try:
                    file = os.path.basename(image)
                    dir = os.path.basename(image)
                    before, sep, after = image.partition(args.l)
                    new_img_location = os.path.splitext(args.d + after)[0] + f".{args.f}"

                    # text for print
                    image_size_is = f"Image {os.path.basename(image)} size is: {round(os.path.getsize(image) / 1024, 2)}KB, New size: {round(os.path.getsize(new_img_location) / 1024, 2)}KB"
                    saved_size = f"Saved: {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))} %"
                    if "Worst" in {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))}:
                        saved_size = f"{Color.select.FAIL}Not Saved!{Color.select.ENDC}"
                    else:
                        saved_size = f"{Color.select.OKBLUE}Saved {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))} %{Color.select.ENDC}"

                    # progress print out
                    print(image_size_is, saved_size)
                except Exception as Err:
                    print(Err)
                    pass

        # end of time measure
        time_end = time.time()

        # final print
        print(f'{Color.select.BOLD}{Color.select.HEADER}Images saved to: {args.d}')
        print(f'{mF.folder_size(args.d)}')
        print(f"Totally edited: {len(image_list)} images, completed within: {round(time_end - time_start, 2)} seconds{Color.select.ENDC}")

    # throwing memory for test purposes. probably ain't do shit.
    iC.gc.collect()

    # once finished exit.
    exit()
