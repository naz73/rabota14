import os

def get_directory_sizes():
    sizes = {}  
  
    for item in os.listdir('.'):
        if os.path.exists(item):
            size = os.path.getsize(item)  
            sizes[item] = size

    return sizes

def main():
    sizes = get_directory_sizes()
    
    sorted_sizes = dict(sorted(sizes.items(), key=lambda item: item[1], reverse=True))

    print("Размеры файлов и директорий в текущей директории:")
    for name, size in sorted_sizes.items():
        print(f"{name} - {size} bytes")

if __name__ == '__main__':
    main()
