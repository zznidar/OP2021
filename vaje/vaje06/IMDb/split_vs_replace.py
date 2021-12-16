# Preverimo, ali je hitrejsi .split(" ") ali .replace(" ", "") -> len
from time import perf_counter

def split(str):
    return(len(str.split(" ")))

def replace(str):
    a = len(str)
    b = len(str.replace(" ", ""))
    return(a-b + 1)

def zanka(str):
    spaces = 0
    for s in str:
        if(s == " "):
            spaces += 1
    return(spaces)

def count(str):
    return(str.count(" "))

def counter(str):
    from collections import Counter
    return(Counter(str).get(" ", 0))

def findall(str):
    import re
    return(len(re.findall(" ", str)))

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel nulla non massa ultrices aliquet in sit amet urna. Aliquam iaculis in neque eu vestibulum. Phasellus dictum aliquam lacus vitae vehicula. Curabitur sit amet fermentum diam. Suspendisse placerat, erat non dignissim egestas, tellus mauris porta lorem, quis gravida turpis purus ut nulla. Nulla pulvinar lobortis arcu ut semper. Pellentesque vel placerat nulla. Donec malesuada varius suscipit. Praesent et diam suscipit, aliquet lacus rutrum, efficitur lacus. Sed a justo erat. Donec nec auctor urna."

t1 = perf_counter()

NoSimulations = 2
loops = 100_000
for i in range(NoSimulations):
    for i in range(loops):
        a = findall(s)
    print(a)
t2 = perf_counter()
print(t2-t1)


## Izkaze se, da je replace hitrejsi:
## replace: 5,47 s
## split: 13,30 s
## zanka: 32,18 s

## Built-in funkcije:
## count: 1,20 s
## Counter: 41,01 s
## findall: 12,54 s
