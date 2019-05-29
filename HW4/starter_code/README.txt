1. Code Illustration
I defined 5 dictionaries in Python for this program. "solved_board" represents the solved
board results, "unassign_row" represents the unassigned entry in each row from A to I, 
"unassign_col" represents the unassigned entry in each column from 1 to 9, "unassign_area"
represents the unassigned entry in each subarea of the board which is divided into 9 
sub-boards of 9x9 size, and "unassign" has the key of each unassigned entry with a set of 
its available values from 1-9 as the value. 
When we choose a variable/entry from "unassign" with minimum remaining values by using a 
priority queue in O(logn) time, we can get its affected entries in its row, column, and 
subarea in O(1) time and then do forward checking. And we update this 5 dictionaries in 
each backtrace recursion. 
The PriorityQueue is defined to find minimum remaining values which can also find and update 
its member. area_idx() function is defined to find the subarea index from 0-8 given a row 
and column number. init_params() function is defined to initialize the 5 dictionaries given 
the initial board. forward_checking() and backtrace() are defined to perform the backtrack 
and forward checking functionalities. And sudokus_start_test() is defined to perform the 
tests on all the boards in "sudokus_start.txt".


2. Test Results:
I solved all 400 boards from "sudokus_start.txt" from line 1 to line 400.
I verified the correctness by converting the solved_board into string and compare it with 
the string line in "sudokus_finish.txt".
The total running time to solve all 400 boards is 2.30810s and the average time to solve 
each board is 0.00577s.

The complete test results are shown below:

board 1: solved board same as sudokus_finish board ? True. Time: 0.00123s
board 2: solved board same as sudokus_finish board ? True. Time: 0.00112s
board 3: solved board same as sudokus_finish board ? True. Time: 0.00282s
board 4: solved board same as sudokus_finish board ? True. Time: 0.00731s
board 5: solved board same as sudokus_finish board ? True. Time: 0.00254s
board 6: solved board same as sudokus_finish board ? True. Time: 0.00342s
board 7: solved board same as sudokus_finish board ? True. Time: 0.00308s
board 8: solved board same as sudokus_finish board ? True. Time: 0.01316s
board 9: solved board same as sudokus_finish board ? True. Time: 0.00549s
board 10: solved board same as sudokus_finish board ? True. Time: 0.00846s
board 11: solved board same as sudokus_finish board ? True. Time: 0.01179s
board 12: solved board same as sudokus_finish board ? True. Time: 0.00405s
board 13: solved board same as sudokus_finish board ? True. Time: 0.01058s
board 14: solved board same as sudokus_finish board ? True. Time: 0.00173s
board 15: solved board same as sudokus_finish board ? True. Time: 0.00785s
board 16: solved board same as sudokus_finish board ? True. Time: 0.00302s
board 17: solved board same as sudokus_finish board ? True. Time: 0.00211s
board 18: solved board same as sudokus_finish board ? True. Time: 0.00250s
board 19: solved board same as sudokus_finish board ? True. Time: 0.01976s
board 20: solved board same as sudokus_finish board ? True. Time: 0.00219s
board 21: solved board same as sudokus_finish board ? True. Time: 0.01709s
board 22: solved board same as sudokus_finish board ? True. Time: 0.00231s
board 23: solved board same as sudokus_finish board ? True. Time: 0.01588s
board 24: solved board same as sudokus_finish board ? True. Time: 0.01187s
board 25: solved board same as sudokus_finish board ? True. Time: 0.01049s
board 26: solved board same as sudokus_finish board ? True. Time: 0.00824s
board 27: solved board same as sudokus_finish board ? True. Time: 0.00668s
board 28: solved board same as sudokus_finish board ? True. Time: 0.00503s
board 29: solved board same as sudokus_finish board ? True. Time: 0.00110s
board 30: solved board same as sudokus_finish board ? True. Time: 0.00134s
board 31: solved board same as sudokus_finish board ? True. Time: 0.00119s
board 32: solved board same as sudokus_finish board ? True. Time: 0.00670s
board 33: solved board same as sudokus_finish board ? True. Time: 0.00116s
board 34: solved board same as sudokus_finish board ? True. Time: 0.00686s
board 35: solved board same as sudokus_finish board ? True. Time: 0.00091s
board 36: solved board same as sudokus_finish board ? True. Time: 0.00348s
board 37: solved board same as sudokus_finish board ? True. Time: 0.00135s
board 38: solved board same as sudokus_finish board ? True. Time: 0.01276s
board 39: solved board same as sudokus_finish board ? True. Time: 0.00355s
board 40: solved board same as sudokus_finish board ? True. Time: 0.00251s
board 41: solved board same as sudokus_finish board ? True. Time: 0.00198s
board 42: solved board same as sudokus_finish board ? True. Time: 0.00282s
board 43: solved board same as sudokus_finish board ? True. Time: 0.00187s
board 44: solved board same as sudokus_finish board ? True. Time: 0.00085s
board 45: solved board same as sudokus_finish board ? True. Time: 0.00888s
board 46: solved board same as sudokus_finish board ? True. Time: 0.00343s
board 47: solved board same as sudokus_finish board ? True. Time: 0.00223s
board 48: solved board same as sudokus_finish board ? True. Time: 0.00127s
board 49: solved board same as sudokus_finish board ? True. Time: 0.00086s
board 50: solved board same as sudokus_finish board ? True. Time: 0.00509s
board 51: solved board same as sudokus_finish board ? True. Time: 0.00095s
board 52: solved board same as sudokus_finish board ? True. Time: 0.00098s
board 53: solved board same as sudokus_finish board ? True. Time: 0.00132s
board 54: solved board same as sudokus_finish board ? True. Time: 0.00084s
board 55: solved board same as sudokus_finish board ? True. Time: 0.00421s
board 56: solved board same as sudokus_finish board ? True. Time: 0.00377s
board 57: solved board same as sudokus_finish board ? True. Time: 0.00264s
board 58: solved board same as sudokus_finish board ? True. Time: 0.00457s
board 59: solved board same as sudokus_finish board ? True. Time: 0.00092s
board 60: solved board same as sudokus_finish board ? True. Time: 0.00770s
board 61: solved board same as sudokus_finish board ? True. Time: 0.01470s
board 62: solved board same as sudokus_finish board ? True. Time: 0.01756s
board 63: solved board same as sudokus_finish board ? True. Time: 0.01491s
board 64: solved board same as sudokus_finish board ? True. Time: 0.00649s
board 65: solved board same as sudokus_finish board ? True. Time: 0.00094s
board 66: solved board same as sudokus_finish board ? True. Time: 0.00326s
board 67: solved board same as sudokus_finish board ? True. Time: 0.02450s
board 68: solved board same as sudokus_finish board ? True. Time: 0.00229s
board 69: solved board same as sudokus_finish board ? True. Time: 0.02069s
board 70: solved board same as sudokus_finish board ? True. Time: 0.00466s
board 71: solved board same as sudokus_finish board ? True. Time: 0.00091s
board 72: solved board same as sudokus_finish board ? True. Time: 0.00209s
board 73: solved board same as sudokus_finish board ? True. Time: 0.00666s
board 74: solved board same as sudokus_finish board ? True. Time: 0.00414s
board 75: solved board same as sudokus_finish board ? True. Time: 0.00650s
board 76: solved board same as sudokus_finish board ? True. Time: 0.00507s
board 77: solved board same as sudokus_finish board ? True. Time: 0.00691s
board 78: solved board same as sudokus_finish board ? True. Time: 0.00187s
board 79: solved board same as sudokus_finish board ? True. Time: 0.00496s
board 80: solved board same as sudokus_finish board ? True. Time: 0.00184s
board 81: solved board same as sudokus_finish board ? True. Time: 0.03611s
board 82: solved board same as sudokus_finish board ? True. Time: 0.00084s
board 83: solved board same as sudokus_finish board ? True. Time: 0.00445s
board 84: solved board same as sudokus_finish board ? True. Time: 0.00418s
board 85: solved board same as sudokus_finish board ? True. Time: 0.00819s
board 86: solved board same as sudokus_finish board ? True. Time: 0.00646s
board 87: solved board same as sudokus_finish board ? True. Time: 0.01231s
board 88: solved board same as sudokus_finish board ? True. Time: 0.00231s
board 89: solved board same as sudokus_finish board ? True. Time: 0.01207s
board 90: solved board same as sudokus_finish board ? True. Time: 0.00176s
board 91: solved board same as sudokus_finish board ? True. Time: 0.00521s
board 92: solved board same as sudokus_finish board ? True. Time: 0.00758s
board 93: solved board same as sudokus_finish board ? True. Time: 0.00287s
board 94: solved board same as sudokus_finish board ? True. Time: 0.01892s
board 95: solved board same as sudokus_finish board ? True. Time: 0.00120s
board 96: solved board same as sudokus_finish board ? True. Time: 0.02261s
board 97: solved board same as sudokus_finish board ? True. Time: 0.01300s
board 98: solved board same as sudokus_finish board ? True. Time: 0.00256s
board 99: solved board same as sudokus_finish board ? True. Time: 0.00356s
board 100: solved board same as sudokus_finish board ? True. Time: 0.00283s
board 101: solved board same as sudokus_finish board ? True. Time: 0.05221s
board 102: solved board same as sudokus_finish board ? True. Time: 0.00973s
board 103: solved board same as sudokus_finish board ? True. Time: 0.00147s
board 104: solved board same as sudokus_finish board ? True. Time: 0.01201s
board 105: solved board same as sudokus_finish board ? True. Time: 0.00340s
board 106: solved board same as sudokus_finish board ? True. Time: 0.00130s
board 107: solved board same as sudokus_finish board ? True. Time: 0.00325s
board 108: solved board same as sudokus_finish board ? True. Time: 0.00113s
board 109: solved board same as sudokus_finish board ? True. Time: 0.00184s
board 110: solved board same as sudokus_finish board ? True. Time: 0.00102s
board 111: solved board same as sudokus_finish board ? True. Time: 0.00296s
board 112: solved board same as sudokus_finish board ? True. Time: 0.00626s
board 113: solved board same as sudokus_finish board ? True. Time: 0.00347s
board 114: solved board same as sudokus_finish board ? True. Time: 0.00121s
board 115: solved board same as sudokus_finish board ? True. Time: 0.00219s
board 116: solved board same as sudokus_finish board ? True. Time: 0.00397s
board 117: solved board same as sudokus_finish board ? True. Time: 0.00147s
board 118: solved board same as sudokus_finish board ? True. Time: 0.00199s
board 119: solved board same as sudokus_finish board ? True. Time: 0.00104s
board 120: solved board same as sudokus_finish board ? True. Time: 0.00376s
board 121: solved board same as sudokus_finish board ? True. Time: 0.00624s
board 122: solved board same as sudokus_finish board ? True. Time: 0.01114s
board 123: solved board same as sudokus_finish board ? True. Time: 0.00151s
board 124: solved board same as sudokus_finish board ? True. Time: 0.01227s
board 125: solved board same as sudokus_finish board ? True. Time: 0.00129s
board 126: solved board same as sudokus_finish board ? True. Time: 0.00709s
board 127: solved board same as sudokus_finish board ? True. Time: 0.00153s
board 128: solved board same as sudokus_finish board ? True. Time: 0.00520s
board 129: solved board same as sudokus_finish board ? True. Time: 0.00086s
board 130: solved board same as sudokus_finish board ? True. Time: 0.00163s
board 131: solved board same as sudokus_finish board ? True. Time: 0.00229s
board 132: solved board same as sudokus_finish board ? True. Time: 0.00272s
board 133: solved board same as sudokus_finish board ? True. Time: 0.00174s
board 134: solved board same as sudokus_finish board ? True. Time: 0.00254s
board 135: solved board same as sudokus_finish board ? True. Time: 0.00394s
board 136: solved board same as sudokus_finish board ? True. Time: 0.00100s
board 137: solved board same as sudokus_finish board ? True. Time: 0.00272s
board 138: solved board same as sudokus_finish board ? True. Time: 0.00746s
board 139: solved board same as sudokus_finish board ? True. Time: 0.00317s
board 140: solved board same as sudokus_finish board ? True. Time: 0.00083s
board 141: solved board same as sudokus_finish board ? True. Time: 0.00098s
board 142: solved board same as sudokus_finish board ? True. Time: 0.00973s
board 143: solved board same as sudokus_finish board ? True. Time: 0.00577s
board 144: solved board same as sudokus_finish board ? True. Time: 0.00119s
board 145: solved board same as sudokus_finish board ? True. Time: 0.01321s
board 146: solved board same as sudokus_finish board ? True. Time: 0.00382s
board 147: solved board same as sudokus_finish board ? True. Time: 0.00166s
board 148: solved board same as sudokus_finish board ? True. Time: 0.02905s
board 149: solved board same as sudokus_finish board ? True. Time: 0.00336s
board 150: solved board same as sudokus_finish board ? True. Time: 0.00137s
board 151: solved board same as sudokus_finish board ? True. Time: 0.01167s
board 152: solved board same as sudokus_finish board ? True. Time: 0.00232s
board 153: solved board same as sudokus_finish board ? True. Time: 0.00343s
board 154: solved board same as sudokus_finish board ? True. Time: 0.00390s
board 155: solved board same as sudokus_finish board ? True. Time: 0.00279s
board 156: solved board same as sudokus_finish board ? True. Time: 0.00288s
board 157: solved board same as sudokus_finish board ? True. Time: 0.03281s
board 158: solved board same as sudokus_finish board ? True. Time: 0.00201s
board 159: solved board same as sudokus_finish board ? True. Time: 0.00330s
board 160: solved board same as sudokus_finish board ? True. Time: 0.00651s
board 161: solved board same as sudokus_finish board ? True. Time: 0.00474s
board 162: solved board same as sudokus_finish board ? True. Time: 0.00133s
board 163: solved board same as sudokus_finish board ? True. Time: 0.01595s
board 164: solved board same as sudokus_finish board ? True. Time: 0.00083s
board 165: solved board same as sudokus_finish board ? True. Time: 0.00712s
board 166: solved board same as sudokus_finish board ? True. Time: 0.02253s
board 167: solved board same as sudokus_finish board ? True. Time: 0.00143s
board 168: solved board same as sudokus_finish board ? True. Time: 0.00833s
board 169: solved board same as sudokus_finish board ? True. Time: 0.01080s
board 170: solved board same as sudokus_finish board ? True. Time: 0.01805s
board 171: solved board same as sudokus_finish board ? True. Time: 0.00148s
board 172: solved board same as sudokus_finish board ? True. Time: 0.00279s
board 173: solved board same as sudokus_finish board ? True. Time: 0.02044s
board 174: solved board same as sudokus_finish board ? True. Time: 0.00367s
board 175: solved board same as sudokus_finish board ? True. Time: 0.00431s
board 176: solved board same as sudokus_finish board ? True. Time: 0.00515s
board 177: solved board same as sudokus_finish board ? True. Time: 0.02042s
board 178: solved board same as sudokus_finish board ? True. Time: 0.00167s
board 179: solved board same as sudokus_finish board ? True. Time: 0.02739s
board 180: solved board same as sudokus_finish board ? True. Time: 0.00932s
board 181: solved board same as sudokus_finish board ? True. Time: 0.00428s
board 182: solved board same as sudokus_finish board ? True. Time: 0.00530s
board 183: solved board same as sudokus_finish board ? True. Time: 0.00178s
board 184: solved board same as sudokus_finish board ? True. Time: 0.00747s
board 185: solved board same as sudokus_finish board ? True. Time: 0.02312s
board 186: solved board same as sudokus_finish board ? True. Time: 0.00537s
board 187: solved board same as sudokus_finish board ? True. Time: 0.00169s
board 188: solved board same as sudokus_finish board ? True. Time: 0.00091s
board 189: solved board same as sudokus_finish board ? True. Time: 0.00119s
board 190: solved board same as sudokus_finish board ? True. Time: 0.00561s
board 191: solved board same as sudokus_finish board ? True. Time: 0.00334s
board 192: solved board same as sudokus_finish board ? True. Time: 0.00224s
board 193: solved board same as sudokus_finish board ? True. Time: 0.00757s
board 194: solved board same as sudokus_finish board ? True. Time: 0.00533s
board 195: solved board same as sudokus_finish board ? True. Time: 0.00354s
board 196: solved board same as sudokus_finish board ? True. Time: 0.00405s
board 197: solved board same as sudokus_finish board ? True. Time: 0.00613s
board 198: solved board same as sudokus_finish board ? True. Time: 0.00351s
board 199: solved board same as sudokus_finish board ? True. Time: 0.00237s
board 200: solved board same as sudokus_finish board ? True. Time: 0.00092s
board 201: solved board same as sudokus_finish board ? True. Time: 0.00129s
board 202: solved board same as sudokus_finish board ? True. Time: 0.00536s
board 203: solved board same as sudokus_finish board ? True. Time: 0.00739s
board 204: solved board same as sudokus_finish board ? True. Time: 0.00480s
board 205: solved board same as sudokus_finish board ? True. Time: 0.00563s
board 206: solved board same as sudokus_finish board ? True. Time: 0.00154s
board 207: solved board same as sudokus_finish board ? True. Time: 0.00165s
board 208: solved board same as sudokus_finish board ? True. Time: 0.00215s
board 209: solved board same as sudokus_finish board ? True. Time: 0.00274s
board 210: solved board same as sudokus_finish board ? True. Time: 0.00631s
board 211: solved board same as sudokus_finish board ? True. Time: 0.00187s
board 212: solved board same as sudokus_finish board ? True. Time: 0.00089s
board 213: solved board same as sudokus_finish board ? True. Time: 0.00202s
board 214: solved board same as sudokus_finish board ? True. Time: 0.00595s
board 215: solved board same as sudokus_finish board ? True. Time: 0.00091s
board 216: solved board same as sudokus_finish board ? True. Time: 0.00425s
board 217: solved board same as sudokus_finish board ? True. Time: 0.00803s
board 218: solved board same as sudokus_finish board ? True. Time: 0.00332s
board 219: solved board same as sudokus_finish board ? True. Time: 0.00121s
board 220: solved board same as sudokus_finish board ? True. Time: 0.01714s
board 221: solved board same as sudokus_finish board ? True. Time: 0.02027s
board 222: solved board same as sudokus_finish board ? True. Time: 0.00794s
board 223: solved board same as sudokus_finish board ? True. Time: 0.00176s
board 224: solved board same as sudokus_finish board ? True. Time: 0.00654s
board 225: solved board same as sudokus_finish board ? True. Time: 0.00113s
board 226: solved board same as sudokus_finish board ? True. Time: 0.01348s
board 227: solved board same as sudokus_finish board ? True. Time: 0.01133s
board 228: solved board same as sudokus_finish board ? True. Time: 0.00833s
board 229: solved board same as sudokus_finish board ? True. Time: 0.00400s
board 230: solved board same as sudokus_finish board ? True. Time: 0.00267s
board 231: solved board same as sudokus_finish board ? True. Time: 0.00308s
board 232: solved board same as sudokus_finish board ? True. Time: 0.00325s
board 233: solved board same as sudokus_finish board ? True. Time: 0.00200s
board 234: solved board same as sudokus_finish board ? True. Time: 0.00348s
board 235: solved board same as sudokus_finish board ? True. Time: 0.02512s
board 236: solved board same as sudokus_finish board ? True. Time: 0.01098s
board 237: solved board same as sudokus_finish board ? True. Time: 0.00378s
board 238: solved board same as sudokus_finish board ? True. Time: 0.00324s
board 239: solved board same as sudokus_finish board ? True. Time: 0.00667s
board 240: solved board same as sudokus_finish board ? True. Time: 0.00418s
board 241: solved board same as sudokus_finish board ? True. Time: 0.00125s
board 242: solved board same as sudokus_finish board ? True. Time: 0.00345s
board 243: solved board same as sudokus_finish board ? True. Time: 0.00183s
board 244: solved board same as sudokus_finish board ? True. Time: 0.00084s
board 245: solved board same as sudokus_finish board ? True. Time: 0.00141s
board 246: solved board same as sudokus_finish board ? True. Time: 0.00929s
board 247: solved board same as sudokus_finish board ? True. Time: 0.01226s
board 248: solved board same as sudokus_finish board ? True. Time: 0.01087s
board 249: solved board same as sudokus_finish board ? True. Time: 0.00187s
board 250: solved board same as sudokus_finish board ? True. Time: 0.01104s
board 251: solved board same as sudokus_finish board ? True. Time: 0.00501s
board 252: solved board same as sudokus_finish board ? True. Time: 0.00656s
board 253: solved board same as sudokus_finish board ? True. Time: 0.00273s
board 254: solved board same as sudokus_finish board ? True. Time: 0.00831s
board 255: solved board same as sudokus_finish board ? True. Time: 0.00314s
board 256: solved board same as sudokus_finish board ? True. Time: 0.00097s
board 257: solved board same as sudokus_finish board ? True. Time: 0.00209s
board 258: solved board same as sudokus_finish board ? True. Time: 0.00510s
board 259: solved board same as sudokus_finish board ? True. Time: 0.00107s
board 260: solved board same as sudokus_finish board ? True. Time: 0.02678s
board 261: solved board same as sudokus_finish board ? True. Time: 0.01032s
board 262: solved board same as sudokus_finish board ? True. Time: 0.00412s
board 263: solved board same as sudokus_finish board ? True. Time: 0.00240s
board 264: solved board same as sudokus_finish board ? True. Time: 0.00374s
board 265: solved board same as sudokus_finish board ? True. Time: 0.00090s
board 266: solved board same as sudokus_finish board ? True. Time: 0.00820s
board 267: solved board same as sudokus_finish board ? True. Time: 0.00254s
board 268: solved board same as sudokus_finish board ? True. Time: 0.00441s
board 269: solved board same as sudokus_finish board ? True. Time: 0.00461s
board 270: solved board same as sudokus_finish board ? True. Time: 0.00635s
board 271: solved board same as sudokus_finish board ? True. Time: 0.00134s
board 272: solved board same as sudokus_finish board ? True. Time: 0.01008s
board 273: solved board same as sudokus_finish board ? True. Time: 0.01057s
board 274: solved board same as sudokus_finish board ? True. Time: 0.00531s
board 275: solved board same as sudokus_finish board ? True. Time: 0.00174s
board 276: solved board same as sudokus_finish board ? True. Time: 0.00806s
board 277: solved board same as sudokus_finish board ? True. Time: 0.00280s
board 278: solved board same as sudokus_finish board ? True. Time: 0.00455s
board 279: solved board same as sudokus_finish board ? True. Time: 0.00986s
board 280: solved board same as sudokus_finish board ? True. Time: 0.00155s
board 281: solved board same as sudokus_finish board ? True. Time: 0.00238s
board 282: solved board same as sudokus_finish board ? True. Time: 0.00226s
board 283: solved board same as sudokus_finish board ? True. Time: 0.00139s
board 284: solved board same as sudokus_finish board ? True. Time: 0.01148s
board 285: solved board same as sudokus_finish board ? True. Time: 0.00238s
board 286: solved board same as sudokus_finish board ? True. Time: 0.00300s
board 287: solved board same as sudokus_finish board ? True. Time: 0.00682s
board 288: solved board same as sudokus_finish board ? True. Time: 0.00110s
board 289: solved board same as sudokus_finish board ? True. Time: 0.00175s
board 290: solved board same as sudokus_finish board ? True. Time: 0.00182s
board 291: solved board same as sudokus_finish board ? True. Time: 0.00531s
board 292: solved board same as sudokus_finish board ? True. Time: 0.00258s
board 293: solved board same as sudokus_finish board ? True. Time: 0.02184s
board 294: solved board same as sudokus_finish board ? True. Time: 0.00258s
board 295: solved board same as sudokus_finish board ? True. Time: 0.00454s
board 296: solved board same as sudokus_finish board ? True. Time: 0.00210s
board 297: solved board same as sudokus_finish board ? True. Time: 0.00591s
board 298: solved board same as sudokus_finish board ? True. Time: 0.00570s
board 299: solved board same as sudokus_finish board ? True. Time: 0.00180s
board 300: solved board same as sudokus_finish board ? True. Time: 0.00141s
board 301: solved board same as sudokus_finish board ? True. Time: 0.00087s
board 302: solved board same as sudokus_finish board ? True. Time: 0.00445s
board 303: solved board same as sudokus_finish board ? True. Time: 0.00085s
board 304: solved board same as sudokus_finish board ? True. Time: 0.00313s
board 305: solved board same as sudokus_finish board ? True. Time: 0.01658s
board 306: solved board same as sudokus_finish board ? True. Time: 0.00101s
board 307: solved board same as sudokus_finish board ? True. Time: 0.00343s
board 308: solved board same as sudokus_finish board ? True. Time: 0.00229s
board 309: solved board same as sudokus_finish board ? True. Time: 0.00691s
board 310: solved board same as sudokus_finish board ? True. Time: 0.00275s
board 311: solved board same as sudokus_finish board ? True. Time: 0.00540s
board 312: solved board same as sudokus_finish board ? True. Time: 0.00163s
board 313: solved board same as sudokus_finish board ? True. Time: 0.02245s
board 314: solved board same as sudokus_finish board ? True. Time: 0.01830s
board 315: solved board same as sudokus_finish board ? True. Time: 0.00082s
board 316: solved board same as sudokus_finish board ? True. Time: 0.00154s
board 317: solved board same as sudokus_finish board ? True. Time: 0.01030s
board 318: solved board same as sudokus_finish board ? True. Time: 0.00085s
board 319: solved board same as sudokus_finish board ? True. Time: 0.00271s
board 320: solved board same as sudokus_finish board ? True. Time: 0.01093s
board 321: solved board same as sudokus_finish board ? True. Time: 0.00167s
board 322: solved board same as sudokus_finish board ? True. Time: 0.00639s
board 323: solved board same as sudokus_finish board ? True. Time: 0.01487s
board 324: solved board same as sudokus_finish board ? True. Time: 0.01426s
board 325: solved board same as sudokus_finish board ? True. Time: 0.00250s
board 326: solved board same as sudokus_finish board ? True. Time: 0.00347s
board 327: solved board same as sudokus_finish board ? True. Time: 0.00574s
board 328: solved board same as sudokus_finish board ? True. Time: 0.00938s
board 329: solved board same as sudokus_finish board ? True. Time: 0.00098s
board 330: solved board same as sudokus_finish board ? True. Time: 0.00409s
board 331: solved board same as sudokus_finish board ? True. Time: 0.01248s
board 332: solved board same as sudokus_finish board ? True. Time: 0.00081s
board 333: solved board same as sudokus_finish board ? True. Time: 0.00175s
board 334: solved board same as sudokus_finish board ? True. Time: 0.00363s
board 335: solved board same as sudokus_finish board ? True. Time: 0.00179s
board 336: solved board same as sudokus_finish board ? True. Time: 0.00416s
board 337: solved board same as sudokus_finish board ? True. Time: 0.00358s
board 338: solved board same as sudokus_finish board ? True. Time: 0.00176s
board 339: solved board same as sudokus_finish board ? True. Time: 0.00157s
board 340: solved board same as sudokus_finish board ? True. Time: 0.00441s
board 341: solved board same as sudokus_finish board ? True. Time: 0.00990s
board 342: solved board same as sudokus_finish board ? True. Time: 0.01268s
board 343: solved board same as sudokus_finish board ? True. Time: 0.00212s
board 344: solved board same as sudokus_finish board ? True. Time: 0.01020s
board 345: solved board same as sudokus_finish board ? True. Time: 0.00788s
board 346: solved board same as sudokus_finish board ? True. Time: 0.00331s
board 347: solved board same as sudokus_finish board ? True. Time: 0.00139s
board 348: solved board same as sudokus_finish board ? True. Time: 0.00426s
board 349: solved board same as sudokus_finish board ? True. Time: 0.00531s
board 350: solved board same as sudokus_finish board ? True. Time: 0.00417s
board 351: solved board same as sudokus_finish board ? True. Time: 0.00179s
board 352: solved board same as sudokus_finish board ? True. Time: 0.00458s
board 353: solved board same as sudokus_finish board ? True. Time: 0.01250s
board 354: solved board same as sudokus_finish board ? True. Time: 0.00536s
board 355: solved board same as sudokus_finish board ? True. Time: 0.00126s
board 356: solved board same as sudokus_finish board ? True. Time: 0.01272s
board 357: solved board same as sudokus_finish board ? True. Time: 0.00197s
board 358: solved board same as sudokus_finish board ? True. Time: 0.00877s
board 359: solved board same as sudokus_finish board ? True. Time: 0.01704s
board 360: solved board same as sudokus_finish board ? True. Time: 0.00167s
board 361: solved board same as sudokus_finish board ? True. Time: 0.00663s
board 362: solved board same as sudokus_finish board ? True. Time: 0.00434s
board 363: solved board same as sudokus_finish board ? True. Time: 0.00085s
board 364: solved board same as sudokus_finish board ? True. Time: 0.00413s
board 365: solved board same as sudokus_finish board ? True. Time: 0.00656s
board 366: solved board same as sudokus_finish board ? True. Time: 0.00412s
board 367: solved board same as sudokus_finish board ? True. Time: 0.00104s
board 368: solved board same as sudokus_finish board ? True. Time: 0.00330s
board 369: solved board same as sudokus_finish board ? True. Time: 0.00200s
board 370: solved board same as sudokus_finish board ? True. Time: 0.01044s
board 371: solved board same as sudokus_finish board ? True. Time: 0.02684s
board 372: solved board same as sudokus_finish board ? True. Time: 0.00257s
board 373: solved board same as sudokus_finish board ? True. Time: 0.00088s
board 374: solved board same as sudokus_finish board ? True. Time: 0.00660s
board 375: solved board same as sudokus_finish board ? True. Time: 0.00165s
board 376: solved board same as sudokus_finish board ? True. Time: 0.00830s
board 377: solved board same as sudokus_finish board ? True. Time: 0.00118s
board 378: solved board same as sudokus_finish board ? True. Time: 0.00329s
board 379: solved board same as sudokus_finish board ? True. Time: 0.00383s
board 380: solved board same as sudokus_finish board ? True. Time: 0.00097s
board 381: solved board same as sudokus_finish board ? True. Time: 0.00971s
board 382: solved board same as sudokus_finish board ? True. Time: 0.00898s
board 383: solved board same as sudokus_finish board ? True. Time: 0.01209s
board 384: solved board same as sudokus_finish board ? True. Time: 0.00147s
board 385: solved board same as sudokus_finish board ? True. Time: 0.00126s
board 386: solved board same as sudokus_finish board ? True. Time: 0.00160s
board 387: solved board same as sudokus_finish board ? True. Time: 0.00380s
board 388: solved board same as sudokus_finish board ? True. Time: 0.00677s
board 389: solved board same as sudokus_finish board ? True. Time: 0.00290s
board 390: solved board same as sudokus_finish board ? True. Time: 0.00173s
board 391: solved board same as sudokus_finish board ? True. Time: 0.00514s
board 392: solved board same as sudokus_finish board ? True. Time: 0.00932s
board 393: solved board same as sudokus_finish board ? True. Time: 0.00219s
board 394: solved board same as sudokus_finish board ? True. Time: 0.00495s
board 395: solved board same as sudokus_finish board ? True. Time: 0.00157s
board 396: solved board same as sudokus_finish board ? True. Time: 0.00460s
board 397: solved board same as sudokus_finish board ? True. Time: 0.00308s
board 398: solved board same as sudokus_finish board ? True. Time: 0.00428s
board 399: solved board same as sudokus_finish board ? True. Time: 0.00222s
board 400: solved board same as sudokus_finish board ? True. Time: 0.01051s
Finishing all boards in file.
Solved 400 of 400 boards in sudokus_start
Total time spent to solve 400 sudoku boards in sudokus_start: 2.30810s
Average time spent to solve 400 sudoku boards in sudokus_start: 0.00577s


3. Hardest sudokus:
It takes 0.22105s to solve the sudoku and verify with the solution.
-> python3 driver_3.py 800000000003600000070090200050007000000045700000100030001000068008500010090000400
-----------------
8 1 2 7 5 3 6 4 9 
9 4 3 6 8 2 1 7 5 
6 7 5 4 9 1 2 8 3 
1 5 4 2 3 7 8 9 6 
3 6 9 8 4 5 7 2 1 
2 8 7 1 6 9 5 3 4 
5 2 1 9 7 4 3 6 8 
4 3 8 5 2 6 9 1 7 
7 9 6 3 1 8 4 5 2 
812753649943682175675491283154237896369845721287169534521974368438526917796318452
Time: 0.22105s