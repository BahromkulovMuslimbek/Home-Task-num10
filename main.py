from multiprocessing import Process, Queue
import requests #Task 6
import os

'''Task num 1'''
# def count_words_in_file(file_path, queue):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#     words = text.lower().split()
#     word_count = len(words)
#     queue.put(word_count)

# def main():
#     current_directory = os.getcwd()
#     txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
#     processes = []
#     queue = Queue()
    
#     for txt_file in txt_files:
#         file_path = os.path.join(current_directory, txt_file)
#         process = Process(target = count_words_in_file, args = (file_path, queue))
#         processes.append(process)
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     total_words = 0
#     while not queue.empty():
#         total_words += queue.get()
    
#     print(f"Barcha filedagi umumiy sozlar soni: {total_words}")


# if __name__ == "__main__":
#     main()



'''Task num 2'''
# def count_nums_in_file(file_path, queue):
#     coun = 0
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         for char in content:
#             if char.isdigit():
#                 coun += 1
#     queue.put((file_path, coun))

# def main():
#     current_directory = os.getcwd()
#     txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
#     processes = []
#     queue = Queue()
    
#     for txt_file in txt_files:
#         file_path = os.path.join(current_directory, txt_file)
#         process = Process(target=count_nums_in_file, args=(file_path, queue))
#         processes.append(process)
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     results = []
#     while not queue.empty():
#         results.append(queue.get())
    
#     for file_path, count in results:
#         print(f"File: {os.path.basename(file_path)}, Raqamlar soni: {count}")


# if __name__ == "__main__":
#     main()



'''Task num 3'''
# def count_sentences_in_file(file_path, queue):
#     coun = 0
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         sentences = content.split('.')
#         coun += len(sentences) - 1
#         sentences = content.split('?')
#         coun += len(sentences) - 1
#         sentences = content.split('!')
#         coun += len(sentences) - 1
#     queue.put(coun)

# def main():
#     current_directory = os.getcwd()
#     txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
#     processes = []
#     queue = Queue()
    
#     for txt_file in txt_files:
#         file_path = os.path.join(current_directory, txt_file)
#         process = Process(target=count_sentences_in_file, args=(file_path, queue))
#         processes.append(process)
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     total_sentences = 0
#     while not queue.empty():
#         total_sentences += queue.get()
    
#     print(f"Barcha filelardagi umumiy gaplar soni: {total_sentences}")


# if __name__ == "__main__":
#     main()



'''Task num 4'''
# def longest_sentence_in_file(file_path, queue):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#     sentences = content.replace('!', '.').replace('?', '.').split('.')
#     longest_sentence = max(sentences, key=len).strip()
#     queue.put((file_path, longest_sentence))

# def main():
#     current_directory = os.getcwd()
#     txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
#     processes = []
#     queue = Queue()
    
#     for txt_file in txt_files:
#         file_path = os.path.join(current_directory, txt_file)
#         process = Process(target = longest_sentence_in_file, args = (file_path, queue))
#         processes.append(process)
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     results = []
#     while not queue.empty():
#         results.append(queue.get())
    
#     for file_path, longest_sentence in results:
#         print(f"File: {os.path.basename(file_path)}, Eng uzun gap: {longest_sentence}")


# if __name__ == "__main__":
#     main()



# '''Task num 5'''
# def clean_special_characters(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
    
#     cleaned_content = ''.join(char for char in content if char.isalnum() or char.isspace())

#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(cleaned_content)

#     print(f"Tozalangan matn: {cleaned_content}")

# def main():
#     current_directory = os.getcwd()
#     txt_files = [f for f in os.listdir(current_directory) if f.endswith('.txt')]
    
#     processes = []
    
#     for txt_file in txt_files:
#         file_path = os.path.join(current_directory, txt_file)
#         process = Process(target=clean_special_characters, args=(file_path,))
#         processes.append(process)
#         process.start()
    
#     for process in processes:
#         process.join()

#     print("Barcha file lar tozalandi")


# if __name__ == "__main__":
#     main()



'''Task num 6'''

image_urls = [
    "https://t4.ftcdn.net/jpg/02/66/31/75/360_F_266317554_kr7DPOoM5Uty0YCeFU9nDZTt4a2LeMJF.jpg"
]

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_name = os.path.basename(url)
        with open(image_name, 'wb') as file:
            file.write(response.content)
        print(f"{image_name} yuklandi.")
    else:
        print(f"{url} dan rasm yuklab olishda hato!")

def main():
    processes = []
    
    for url in image_urls:
        process = Process(target = download_image, args = (url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("Barcha rasmlar yuklandi")


if __name__ == "__main__":
    main()