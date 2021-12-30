from prijatelji import *

mrezje = {"Ana": {"Janez", "Andrej", "Katja"},
"Janez": {"Ana", "Andrej", "Jaka"},
"Katja": {"Ana", "Jaka"},
"Jaka": {"Janez", "Katja"},
"Andrej": {"Ana", "Janez"},
}

print(prijatelji_od(mrezje, "Ana"))