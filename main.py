from components import imageCompressor as iC, mainFunctions as mF, localColors as Color
import concurrent.futures
import argparse
import time
import os

# 👇️ measuring number of cores in your machine. Will utilize all of them. you can set cores manually such as n_cores = 4
n_cores = os.cpu_count()

# 👇️ starting everything
if __name__ == '__main__':
    # 👇️ passing commands to command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', type=str, required=True)  # images locations
    parser.add_argument('-d', type=str, required=True)  # images destination
    parser.add_argument('-f', type=str, required=True)  # images format
    parser.add_argument('-w', type=int, required=True)  # images max width
    parser.add_argument('-q', type=int, required=True)  # images quality
    parser.add_argument('-r', type=str)  # remove larger files y/n
    args = parser.parse_args()

    # 👇️ begging of time measure
    time_start = time.time()

    # 👇️ building list of files from generator function
    image_list = [file for file in mF.build_file_list(args.l)]

    # 👇️ starting multicore image processing loop
    with concurrent.futures.ProcessPoolExecutor(max_workers=n_cores) as executor:
        # Start the load operations and mark each future with its URL
        future_to_image = {executor.submit(mF.start_command, image, args.l, args.d, dformat=args.f, max_width=args.w,
                                           quality=args.q): image
                           for image in image_list}

        # 👇️ returning output from pool
        for future in concurrent.futures.as_completed(future_to_image):
            image = future_to_image[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (image, exc))
            else:
                try:
                    file = os.path.basename(image)  # original image file name
                    before, sep, after = image.partition(args.l)  # remove location from image if you use after.
                    new_img_location = os.path.splitext(args.d + after)[0] + f".{args.f}"  # new image full Path

                    # 👇️ text for print
                    image_size_is = f"Image {os.path.basename(image)} size is: {round(os.path.getsize(image) / 1024, 2)}KB, new size: {round(os.path.getsize(new_img_location) / 1024, 2)}KB"
                    saved_size = f"Saved: {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))} %"
                    if mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location)) < 0:
                        saved_size = f"{Color.select.FAIL}, worst by {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))}%{Color.select.ENDC}"
                        # 👇️ will remove larger files if you selected yes.
                        try:
                            if args.r.lower() == "y":
                                os.remove(new_img_location)
                                print(
                                    f"{Color.select.WARNING}The file below: {os.path.basename(new_img_location)} was removed is{Color.select.ENDC}{saved_size}")
                            else:
                                continue
                        except Exception as Err:
                            _ = Err
                            pass
                    else:
                        saved_size = f"{Color.select.OKBLUE} saved {mF.get_percentage_difference(os.path.getsize(image), os.path.getsize(new_img_location))}%{Color.select.ENDC}"

                    # 👇️ progress print out
                    print(f'{image_size_is}{saved_size}')

                except Exception as Err:
                    print(Err)
                    pass

        # 👇️ end of time measure
        time_end = time.time()

        # 👇️ final print
        print(f'{Color.select.BOLD}{Color.select.HEADER}Images saved to: {args.d}')
        print(f'{mF.folder_size(args.d)}')
        print(
            f"Totally processed: {len(image_list)} images, completed within: {round(time_end - time_start, 2)} seconds{Color.select.ENDC}")

    # 👇️ throwing memory for test purposes. probably ain't do shit.
    iC.gc.collect()

    # 👇️ once finished exit.
    exit()
