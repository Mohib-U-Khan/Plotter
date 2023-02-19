import serial
import time

my_str = "U 4 3 D 3 15 3 26 3 38 3 50 3 62 3 73 4 85 4 97 4 109 4 121 4 133 4 145 4 157 4 170 4 182 4 194 3 206 3 218 3 230 3 242 3 254 3 266 3 278 3 290 3 302 3 314 4 327 4 339 3 352 3 364 3 375 4 387 4 399 4 411 4 422 4 434 4 446 4 458 4 471 4 483 11 489 23 489 35 489 48 488 60 488 72 488 84 488 96 488 108 468 119 431 132 395 U 144 352 D 156 317 U 153 299 D 141 290 129 281 117 274 105 265 93 256 81 247 69 238 57 230 45 222 33 213 21 204 9 196 U 8 199 D 24 211 41 223 57 235 74 247 91 259 107 271 124 282 140 294 157 306 157 318 152 330 149 342 144 354 139 366 136 378 132 390 128 402 124 413 119 425 116 437 112 449 109 461 104 474 100 486 116 479 128 470 140 461 152 452 163 444 176 435 188 426 200 417 212 410 225 401 237 392 249 383 262 378 274 387 286 395 298 404 310 413 322 422 334 429 346 438 358 448 370 457 382 464 394 473 406 482 U 404 446 D 392 409 380 373 U 372 348 D 360 312 U 355 308 D 367 297 379 288 391 280 403 271 415 262 426 253 438 246 450 237 462 228 474 219 486 210 498 201 512 199 512 212 512 224 512 236 512 248 512 260 511 272 511 283 511 296 511 307 512 320 512 332 512 344 512 356 512 368 513 380 513 392 513 404 513 416 513 428 512 440 512 452 512 464 512 476 U 510 489 D 498 489 485 489 473 488 461 488 449 488 437 488 425 488 413 486 408 474 404 462 401 450 396 438 392 426 389 413 384 401 381 389 377 378 372 366 369 354 364 342 361 330 357 318 355 305 372 292 388 280 405 268 421 256 439 244 453 231 470 219 487 207 505 195 511 179 511 167 510 155 511 143 511 131 511 119 511 107 511 95 511 83 511 72 511 60 511 48 511 36 512 24 512 12 506 2 494 2 482 2 470 2 457 2 445 2 433 3 421 2 410 2 398 3 386 2 374 2 362 2 350 2 338 2 325 3 313 3 301 4 290 4 277 4 266 3 254 3 242 3 230 3 218 3 205 3 193 4 181 4 169 4 158 4 146 4 134 5 122 5 110 5 98 4 86 4 74 4 62 4 49 4 37 4 25 4 13 4 1 4 U 5 190 D 17 190 29 190 41 190 53 190 65 190 77 190 89 190 101 190 113 190 125 189 137 189 149 189 161 189 173 189 185 189 197 189 209 153 221 116 233 78 245 41 265 14 277 51 289 87 301 124 313 162 325 188 337 189 349 189 361 189 373 189 385 189 397 189 409 189 421 189 433 189 444 189 456 189 467 189 479 189 491 189 503 189 U 315 182 D 311 171 306 159 303 147 299 136 296 123 292 111 287 99 285 87 280 75 277 63 272 51 269 39 265 27 262 15 U 256 6 D 252 18 249 30 245 42 242 55 238 67 233 79 230 90 225 102 222 114 218 126 214 138 211 150 206 162 203 174 199 186 U 256 380 D 240 392 222 404 205 416 189 427 173 439 156 451 140 463 123 476 116 489 128 489 140 489 152 489 164 489 176 488 188 488 200 488 212 487 224 487 236 487 248 488 259 487 271 487 283 487 295 487 306 487 319 487 331 487 343 488 355 487 367 487 379 487 391 487 U 396 482 D 380 470 363 458 345 445 328 434 311 421 294 409 278 397 262 385"

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
def write_to_arduino():
    d = 'U '
    s =  [d+e for e in my_str.split(d) if e]

    print(s)

    for ss in s:
        arduino.write(bytes(ss, 'utf-8'))
        time.sleep(5)

    # while(not arduino.readable()):
    #     pass
    # while (arduino.readable):
    #     print (f'recvd message {arduino.read_all()}')

write_to_arduino()
# arduino.write(bytes('q', 'utf-8'))