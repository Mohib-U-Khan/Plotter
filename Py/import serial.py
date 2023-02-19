import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
# image_to_binarray.WriteOutImage()
my_str = "U 65 2 D 64 14 65 26 71 38 88 39 100 39 112 39 124 41 136 42 148 39 160 29 172 24 184 26 196 30 208 41 220 39 232 39 244 40 256 41 268 44 281 46 293 55 304 61 312 64 324 69 338 64 350 64 364 73 370 61 382 59 394 63 407 68 U 405 80 D 373 111 U 371 135 D 405 103 U 430 112 D 396 145 364 176 U 365 174 D 366 186 360 198 367 199 367 221 371 233 377 256 U 373 238 D 405 206 U 401 178 D 432 146 464 113 U 426 132 D 392 133 359 134 U 345 137 D 331 161 U 319 179 D 307 200 305 202 313 190 323 171 332 155 341 140 353 132 343 121 350 119 348 107 353 95 343 83 335 79 U 332 78 D 344 73 356 73 360 76 363 80 378 79 390 80 402 80 U 399 59 D 368 61 337 60 U 328 63 D 316 62 U 300 75 D 293 64 U 273 51 D 262 50 U 216 53 D 184 54 152 54 U 154 69 D 166 66 177 67 170 80 158 86 U 144 86 D 159 82 155 64 143 73 U 148 95 D 145 82 144 70 140 59 125 43 U 77 40 D 46 40 14 40 U 16 48 D 48 16 U 66 3 D 78 4 90 3 102 3 113 3 125 3 137 3 148 3 160 3 172 3 184 3 196 3 208 4 220 4 232 4 244 4 256 4 269 3 281 3 293 3 304 3 317 3 328 3 340 2 352 2 364 2 376 2 388 1 400 2 413 2 425 2 436 2 448 2 460 3 473 3 485 4 497 4 508 4 511 15 511 26 511 38 511 50 511 62 511 74 511 86 512 98 512 110 512 122 512 134 513 146 513 159 513 171 513 183 513 195 513 207 513 219 513 231 513 243 513 255 513 266 513 278 U 530 312 D 495 312 462 313 U 465 336 D 496 337 530 338 U 535 379 D 505 377 U 495 405 D 464 405 U 450 416 D 434 407 422 411 409 408 397 401 U 396 400 D 365 432 U 362 437 D 394 436 424 435 456 435 488 435 U 499 456 D 466 488 431 521 397 552 362 584 U 368 586 D 399 584 U 390 577 D 402 555 414 554 427 557 439 559 454 571 463 583 466 595 456 607 445 619 448 640 439 658 428 660 431 673 419 685 436 700 456 712 470 718 U 460 720 D 492 688 U 465 684 D 498 652 U 493 641 D 505 641 U 519 628 D 488 629 454 631 420 635 388 637 U 393 642 D 405 651 413 671 425 674 U 431 663 D 443 655 462 649 472 661 483 673 492 685 499 697 501 709 496 717 498 729 U 485 730 D 520 729 U 500 712 D 488 717 U 530 696 D 497 697 464 699 432 700 U 426 693 D 457 662 U 455 658 D 443 670 458 682 460 694 U 456 678 D 444 673 U 441 642 D 429 639 U 421 625 D 433 619 U 438 622 D 405 653 U 398 620 D 429 588 U 432 599 D 444 610 U 443 600 D 455 607 463 591 470 602 U 494 594 D 526 561 U 526 567 D 496 569 465 568 431 571 399 573 367 574 336 575 305 575 U 305 603 D 337 602 369 602 401 602 433 600 466 599 499 598 529 596 U 530 588 D 497 589 U 507 610 D 494 618 U 480 653 D 470 644 458 630 U 455 631 D 463 643 473 653 484 665 490 674 500 686 507 698 U 453 782 D 422 812 393 844 362 875 U 389 873 D 421 839 453 809 U 429 812 D 441 817 453 821 465 822 477 826 493 830 506 830 U 501 841 D 468 873 U 497 881 D 529 850 U 501 808 D 467 840 434 872 U 396 868 D 428 870 460 870 495 870 U 432 784 D 399 814 365 845 331 876 U 332 870 D 320 862 U 306 878 D 336 847 367 816 398 784 U 394 777 D 390 765 U 399 755 D 366 786 334 817 304 846 276 875 U 301 874 D 313 874 325 874 U 339 845 D 309 845 279 846 U 237 860 D 269 861 301 862 335 863 369 865 U 415 845 D 394 834 387 812 U 388 811 D 390 823 394 835 U 365 803 D 333 802 U 329 802 D 326 793 321 794 315 797 319 809 328 820 338 832 353 844 U 386 856 D 375 853 362 848 350 840 339 829 327 815 315 792 U 321 774 D 306 786 293 798 280 810 283 807 295 796 307 785 319 775 333 805 345 818 357 830 369 834 380 841 392 843 392 848 U 371 844 D 356 832 350 831 346 824 337 818 331 806 U 278 794 D 308 793 341 792 374 792 405 791 436 791 467 792 500 791 U 366 753 D 334 784 301 814 267 845 232 875 U 196 845 D 200 837 184 840 190 846 178 858 158 870 U 166 873 D 178 873 189 870 201 859 213 849 225 840 237 830 249 820 261 807 272 796 284 786 296 775 308 766 321 756 333 747 345 736 357 725 U 354 734 D 338 751 326 767 314 774 302 783 290 794 278 805 265 820 253 826 243 846 249 834 264 822 275 810 285 798 299 786 314 775 331 763 338 751 353 739 U 352 741 D 346 753 344 754 U 366 737 D 368 749 372 762 375 774 376 786 U 329 719 D 363 720 397 720 430 720 U 391 692 D 360 691 327 693 U 350 684 D 353 696 356 708 360 720 348 732 335 744 319 757 304 769 291 781 276 793 263 805 252 816 239 828 225 841 210 853 197 865 U 244 784 D 212 784 179 783 147 784 U 151 755 D 183 755 213 754 243 754 U 236 744 D 239 756 244 768 U 301 752 D 335 753 368 752 400 752 431 755 462 755 U 523 656 D 490 654 457 656 424 657 393 657 361 655 331 654 U 359 646 D 354 649 355 661 350 673 346 685 332 697 320 708 306 720 295 732 283 743 270 755 267 758 278 747 290 736 302 724 314 714 326 702 337 690 349 669 362 666 365 676 U 363 628 D 332 629 298 629 U 271 627 D 254 639 265 631 U 240 663 D 209 664 175 665 U 174 671 D 162 664 U 155 676 D 165 684 150 695 138 708 152 725 164 716 165 722 177 708 190 699 191 674 194 652 205 657 U 198 638 D 186 646 174 652 162 659 151 674 139 683 128 692 119 701 131 689 146 678 152 667 161 661 179 649 200 637 U 203 682 D 195 682 184 686 158 698 U 175 700 D 207 698 240 695 U 254 695 D 254 708 U 238 730 D 207 728 175 727 U 152 726 D 169 714 175 702 U 205 689 D 217 688 205 685 205 696 192 705 196 713 181 719 165 730 151 742 139 754 145 748 157 739 177 726 189 723 196 723 210 707 201 725 204 736 192 746 176 748 159 760 144 771 147 783 158 774 149 765 160 759 172 751 183 751 196 739 201 730 222 733 207 744 192 750 170 757 159 771 U 213 738 D 200 744 182 751 183 739 182 726 202 718 218 711 U 160 693 D 148 699 136 707 U 111 821 D 143 822 176 821 208 821 238 821 271 821 301 820 332 819 363 819 396 818 428 815 460 817 492 817 527 817 U 459 599 D 490 567 520 535 U 501 527 D 469 559 U 471 556 D 441 557 410 560 378 561 U 365 559 D 399 527 429 496 459 465 U 449 450 D 428 462 432 454 438 440 434 427 435 415 419 420 410 419 402 417 389 402 404 390 418 378 412 372 399 372 387 370 375 370 363 373 U 362 372 D 394 372 425 372 U 440 397 D 452 395 454 404 456 416 453 428 460 440 U 479 438 D 477 426 474 414 471 402 469 390 466 378 464 366 460 353 459 342 458 330 454 318 452 306 449 297 440 283 435 275 439 282 U 466 283 D 498 283 U 466 244 D 435 247 U 429 247 D 438 247 434 259 447 265 468 277 485 289 504 301 512 313 512 325 512 337 512 350 512 362 512 374 512 386 U 503 386 D 491 379 479 370 468 361 U 472 367 D 487 379 503 391 512 403 512 415 512 427 512 439 512 451 491 463 489 467 U 524 470 D 491 471 459 473 427 473 392 473 357 475 325 474 U 335 476 D 341 469 337 475 337 487 340 499 U 330 501 D 362 500 395 500 428 500 460 500 491 500 523 500 U 521 532 D 487 532 455 532 424 533 393 534 361 535 328 535 U 334 525 D 365 494 U 377 478 D 389 484 U 366 492 D 344 497 352 492 356 480 355 468 352 455 U 359 471 D 359 483 U 365 521 D 397 519 430 520 463 521 U 456 525 D 452 525 466 513 462 514 449 519 U 460 501 D 472 498 484 495 496 495 508 495 513 507 U 512 522 D 502 518 502 506 490 503 U 483 506 D 488 518 488 515 U 490 524 D 480 509 479 505 U 450 548 D 462 541 470 534 471 548 483 557 U 508 563 D 509 570 498 586 501 598 498 615 507 625 510 637 511 649 512 661 512 673 507 685 512 696 510 713 511 725 511 737 512 749 512 761 512 773 512 785 512 797 512 809 512 821 513 833 512 845 512 857 512 868 U 519 847 D 488 848 454 850 420 854 388 856 356 856 324 856 294 856 264 858 233 857 203 857 173 856 143 857 112 860 80 861 U 49 855 D 17 858 U 5 819 D 17 850 29 874 41 874 53 873 65 873 77 873 89 873 102 873 113 873 125 873 137 873 149 867 161 858 173 848 185 839 197 830 209 821 221 814 U 366 609 D 381 598 391 610 390 622 390 634 390 646 397 655 405 667 411 679 414 690 424 687 436 696 448 704 U 510 593 D 495 605 483 612 470 621 478 610 489 602 478 598 476 582 469 582 469 570 468 552 456 557 U 443 563 D 455 570 464 582 480 577 492 585 503 581 U 432 576 D 433 588 426 608 422 623 419 635 419 647 421 659 425 671 436 666 446 669 450 658 460 646 471 655 483 664 490 679 494 685 508 699 U 412 586 D 418 574 418 573 U 422 571 D 426 583 437 596 443 608 U 405 597 D 397 585 393 573 399 561 409 549 406 575 U 413 555 D 406 567 404 579 414 586 424 593 436 589 442 571 U 430 558 D 462 526 495 495 527 464 U 507 450 D 496 457 484 460 472 464 460 460 448 456 432 472 420 474 407 467 398 485 384 474 404 468 405 455 405 443 404 427 392 426 373 429 369 426 351 425 348 424 345 424 343 426 332 426 U 335 423 D 335 435 334 446 344 431 356 434 U 367 414 D 361 419 349 417 337 417 U 336 416 D 330 403 341 408 353 406 366 406 378 409 383 426 U 372 398 D 376 398 388 407 394 396 407 389 U 426 405 D 424 417 U 426 409 D 393 410 362 411 330 412 U 324 397 D 336 395 348 388 360 382 369 394 381 403 369 423 364 440 346 458 371 458 368 468 374 472 372 485 365 497 353 506 351 518 350 530 349 542 U 352 562 D 364 576 376 587 388 595 U 363 626 D 365 614 371 602 375 590 363 578 349 566 U 368 530 D 400 500 433 468 U 438 457 D 434 469 431 495 431 507 435 510 U 428 447 D 416 447 405 451 421 441 U 388 458 D 384 449 375 460 362 452 351 445 343 459 340 451 328 454 U 303 463 D 291 457 U 292 458 D 278 450 266 441 U 257 450 D 253 462 257 450 269 440 281 447 293 454 U 289 452 D 312 464 U 306 480 D 304 492 293 510 288 524 U 267 520 D 255 512 243 500 U 241 498 D 253 505 265 514 277 521 289 518 301 498 U 332 523 D 344 549 U 274 520 D 252 508 242 496 239 492 245 480 252 474 240 492 U 250 504 D 262 516 281 528 U 164 508 D 152 470 U 137 453 D 125 449 U 121 444 D 133 417 141 436 143 448 U 143 435 D 132 400 120 365 U 110 340 D 114 352 119 366 124 379 128 392 131 404 132 419 126 430 121 442 132 454 150 467 153 479 157 490 160 502 164 514 167 526 172 538 176 550 180 562 184 575 188 587 193 599 197 613 U 192 371 D 204 378 215 387 227 396 239 405 251 385 263 355 U 258 348 D 246 338 U 257 339 D 238 329 U 220 317 D 235 329 246 338 262 344 262 356 258 368 252 379 247 392 242 404 U 207 384 D 192 370 U 185 365 D 197 343 210 321 222 309 234 319 246 328 258 339 270 348 U 247 401 D 239 414 230 404 214 392 199 380 187 368 193 356 199 345 206 333 212 320 218 308 U 233 243 D 202 243 171 243 140 242 108 243 76 243 45 244 14 244 U 10 239 D 12 251 21 259 33 257 42 265 52 263 64 271 76 278 81 283 U 83 269 D 94 299 U 108 307 D 76 307 46 306 15 308 U 8 308 D 20 300 U 17 300 D 48 270 U 43 277 D 45 283 43 278 47 266 32 281 U 10 280 D 43 278 75 277 109 275 U 91 258 D 79 264 U 82 264 D 79 276 84 290 84 305 83 319 U 76 333 D 43 364 U 63 337 D 74 328 69 340 72 343 U 75 342 D 41 342 7 344 U 14 343 D 22 338 17 328 U 20 321 D 22 313 34 315 46 317 62 305 71 309 83 306 U 78 293 D 65 296 53 299 45 296 34 305 23 309 11 317 17 319 U 5 332 D 12 326 11 338 9 346 23 344 24 333 36 341 U 56 277 D 43 291 31 286 24 279 12 275 12 269 U 2 272 D 23 268 22 280 24 295 23 304 13 316 8 328 9 340 31 361 57 373 63 359 U 55 365 D 66 362 68 350 56 344 53 342 68 335 71 323 65 321 54 351 48 363 58 352 44 355 59 347 64 335 64 326 57 323 43 337 39 356 42 348 43 336 47 323 58 320 56 304 51 294 33 291 40 279 42 275 34 272 41 257 29 250 17 245 5 235 U 21 214 D 33 218 45 224 57 232 70 239 84 245 U 83 246 D 90 253 U 53 232 D 41 224 U 47 226 D 60 238 82 248 95 255 108 257 120 256 132 252 143 252 155 246 167 243 172 245 185 250 197 250 209 250 221 247 233 247 245 245 U 216 235 D 205 238 188 231 176 231 U 174 227 D 186 225 197 225 209 225 221 225 230 218 242 217 247 229 258 229 271 225 283 222 295 221 303 225 316 246 328 243 341 242 353 239 359 241 365 235 377 249 U 396 249 D 364 250 333 252 U 316 252 D 328 258 340 256 352 253 364 250 U 388 245 D 382 257 384 248 392 242 395 230 397 224 397 212 396 203 393 191 402 174 400 162 403 150 400 158 U 407 155 D 413 167 416 179 419 191 420 203 425 215 432 230 423 243 426 255 429 267 431 279 433 291 436 303 440 315 445 328 446 340 451 351 455 363 458 375 461 387 463 398 466 410 467 423 470 435 U 466 438 D 450 427 443 422 440 408 443 395 U 367 370 D 361 382 U 348 370 D 353 363 350 357 338 352 U 341 350 D 344 361 346 373 349 385 326 396 327 408 329 420 329 432 329 444 326 456 321 468 321 480 321 492 322 504 326 516 329 528 335 539 343 551 343 563 340 575 336 587 328 599 313 612 316 609 328 600 338 581 U 500 296 D 488 289 476 281 465 273 453 265 442 254 U 429 253 D 449 255 468 267 486 279 506 292 U 505 286 D 493 278 481 271 469 263 457 255 445 247 427 235 418 236 407 236 U 426 206 D 394 207 360 208 327 209 296 208 265 208 234 207 204 206 175 208 144 208 112 207 80 206 48 206 18 206 U 12 179 D 44 179 76 176 108 177 142 178 176 178 206 177 239 177 271 175 302 174 333 173 365 174 398 172 430 172 U 430 139 D 397 139 363 139 329 138 297 140 265 140 232 140 200 140 168 140 136 143 104 145 72 147 41 147 10 147 U 9 116 D 42 116 75 117 106 116 138 115 171 114 201 115 231 116 263 115 296 112 327 112 360 110 391 111 423 110 455 107 U 457 75 D 424 76 393 76 361 74 331 73 298 74 264 75 232 77 201 81 170 84 140 85 109 87 78 89 49 89 17 88 U 5 49 D 17 50 29 50 41 50 54 50 66 51 78 51 90 51 102 52 114 53 126 52 137 49 147 57 158 57 167 57 179 56 191 57 203 57 U 212 61 D 216 73 213 79 186 84 177 95 181 93 192 95 203 98 U 218 94 D 217 82 U 191 72 D 179 69 U 202 41 D 185 29 U 186 27 D 202 39 205 55 206 72 183 69 197 72 185 82 171 91 155 94 153 96 167 96 171 91 173 82 185 85 188 89 195 77 203 71 215 78 210 102 U 275 60 D 263 59 250 57 238 57 226 58 214 56 198 44 186 44 174 42 162 42 151 36 169 24 U 82 14 D 49 44 U 7 21 D 40 21 71 21 104 20 U 80 29 D 81 17 81 5 U 62 38 D 50 38 39 36 27 36 15 35 3 29 U 3 27 D 2 39 2 51 2 63 2 74 2 86 2 98 2 110 2 122 3 134 3 146 3 158 3 170 3 183 3 195 4 207 4 219 4 232 4 244 4 256 7 259 17 271 4 277 7 289 5 300 4 311 4 323 4 335 4 347 4 359 4 371 4 383 4 394 4 407 4 419 4 431 3 443 3 455 3 467 3 479 3 491 3 503 3 515 3 527 3 539 3 552 3 564 3 576 3 589 4 601 4 613 4 625 4 636 4 648 4 660 4 672 4 683 4 695 4 707 4 718 4 731 5 743 5 755 5 767 4 779 4 791 4 803 4 815 5 827 9 840 14 852 18 864 U 146 250 D 177 237 176 225 U 300 225 D 306 238 311 250 315 262 U 353 214 D 349 226 349 202 361 173 373 181 385 176 397 175 U 390 173 D 379 188 390 200 387 210 384 222 382 224 397 228 414 226 429 218 U 393 206 D 381 189 U 382 206 D 370 204 U 382 216 D 370 221 352 217 348 233 342 220 347 209 351 197 357 185 362 173 U 398 146 D 410 138 422 137 434 127 442 110 U 449 92 D 447 86 436 84 423 87 411 96 415 95 427 77 435 78 438 66 426 63 U 437 67 D 449 69 U 445 71 D 455 83 452 102 442 113 440 122 426 134 U 428 82 D 415 80 403 85 391 88 379 87 367 84 U 370 18 D 337 20 U 319 5 D 316 17 314 29 311 41 307 53 303 66";

ss = '0 0 0 1536 1536 1536 1536 0 0 0'
0 0 0 1024 1024 1024 1024 0 0 0 512 512 512 1024 1024 1024 1024 512 512 512
0 0 0 1024 1024 1024 1024 0 0 0     
x = 'q'

start star

U 4 3 D 3 15 3 26 3 38 3 50 3 62 3 73 4 85 4 97 4 109 4 121 4 133 4 145 4 157 4 170 4 182 4 194 3 206 3 218 3 230 3 242 3 254 3 266 3 278 3 290 3 302 3 314 4 327 4 339 3 352 3 364 3 375 4 387 4 399 4 411 4 422 4 434 4 446 4 458 4 471 4 483 11 489 23 489 35 489 48 488 60 488 72 488 84 488 96 488 108 468 119 431 132 395 U 144 352 D 156 317 U 153 299 D 141 290 129 281 117 274 105 265 93 256 81 247 69 238 57 230 45 222 33 213 21 204 9 196 

U 8 199 D 24 211 41 223 57 235 74 247 91 259 107 271 124 282 140 294 157 306 157 318 152 330 149 342 144 354 139 366 136 378 132 390 128 402 124 413 119 425 116 437 112 449 109 461 104 474 100 486 116 479 128 470 140 461 152 452 163 444 176 435 188 426 200 417 212 410 225 401 237 392 249 383 262 378 274 387 286 395 298 404 310 413 322 422 334 429 346 438 358 448 370 457 382 464 394 473 406 482 U 404 446 D 392 409 380 373 U 372 348 D 360 312 

U 355 308 D 367 297 379 288 391 280 403 271 415 262 426 253 438 246 450 237 462 228 474 219 486 210 498 201 512 199 512 212 512 224 512 236 512 248 512 260 511 272 511 283 511 296 511 307 512 320 512 332 512 344 512 356 512 368 513 380 513 392 513 404 513 416 513 428 512 440 512 452 512 464 512 476 

U 510 489 D 498 489 485 489 473 488 461 488 449 488 437 488 425 488 413 486 408 474 404 462 401 450 396 438 392 426 389 413 384 401 381 389 377 378 372 366 369 354 364 342 361 330 357 318 355 305 372 292 388 280 405 268 421 256 439 244 453 231 470 219 487 207 505 195 511 179 511 167 510 155 511 143 511 131 511 119 511 107 511 95 511 83 511 72 511 60 511 48 511 36 512 24 512 12 506 2 494 2 482 2 470 2 457 2 445 2 433 3 421 2 410 2 398 3 386 2 374 2 362 2 350 2 338 2 325 3 313 3 301 4 290 4 277 4 266 3 254 3 242 3 230 3 218 3 205 3 193 4 181 4 169 4 158 4 146 4 134 5 122 5 110 5 98 4 86 4 74 4 62 4 49 4 37 4 25 4 13 4 1 4 

U 5 190 D 17 190 29 190 41 190 53 190 65 190 77 190 89 190 101 190 113 190 125 189 137 189 149 189 161 189 173 189 185 189 197 189 209 153 221 116 233 78 245 41 265 14 277 51 289 87 301 124 313 162 325 188 337 189 349 189 361 189 373 189 385 189 397 189 409 189 421 189 433 189 444 189 456 189 467 189 479 189 491 189 503 189 

U 315 182 D 311 171 306 159 303 147 299 136 296 123 292 111 287 99 285 87 280 75 277 63 272 51 269 39 265 27 262 15 U 256 6 D 252 18 249 30 245 42 242 55 238 67 233 79 230 90 225 102 222 114 218 126 214 138 211 150 206 162 203 174 199 186 

U 256 380 D 240 392 222 404 205 416 189 427 173 439 156 451 140 463 123 476 116 489 128 489 140 489 152 489 164 489 176 488 188 488 200 488 212 487 224 487 236 487 248 488 259 487 271 487 283 487 295 487 306 487 319 487 331 487 343 488 355 487 367 487 379 487 391 487 U 396 482 D 380 470 363 458 345 445 328 434 311 421 294 409 278 397 262 385  

end star

U 4 3 D 3 15 3 26 3 38 3 50 3 62 3 73 4 85 4 97 4 109 4 121 4 133 4 145 4 157 4 170 4 182 4 194 3 206 3 218 3 230 3 242 3 254 3 266 3 278 3 290 3 302 3 314 4 327 4 339 3 352 3 364 3 375 4 387 4 399 4 411 4 422 4 434 4 446 4 458 4 471 4 483 11 489 23 489 35 489 48 488 60 488 72 488 84 488 96 488 108 468 119 431 132 395 U 144 352 D 156 317 U 153 299 D 141 290 129 281 117 274 105 265 93 256 81 247 69 238 57 230 45 222 33 213 21 204 9 196 U 8 199 D 24 211 41 223 57 235 74 247 91 259 107 271 124 282 140 294 157 306 157 318 152 330 149 342 144 354 139 366 136 378 132 390 128 402 124 413 119 425 116 437 112 449 109 461 104 474 100 486 116 479 128 470 140 461 152 452 163 444 176 435 188 426 200 417 212 410 225 401 237 392 249 383 262 378 274 387 286 395 298 404 310 413 322 422 334 429 346 438 358 448 370 457 382 464 394 473 406 482 U 404 446 D 392 409 380 373 U 372 348 D 360 312 U 355 308 D 367 297 379 288 391 280 403 271 415 262 426 253 438 246 450 237 462 228 474 219 486 210 498 201 512 199 512 212 512 224 512 236 512 248 512 260 511 272 511 283 511 296 511 307 512 320 512 332 512 344 512 356 512 368 513 380 513 392 513 404 513 416 513 428 512 440 512 452 512 464 512 476 U 510 489 D 498 489 485 489 473 488 461 488 449 488 437 488 425 488 413 486 408 474 404 462 401 450 396 438 392 426 389 413 384 401 381 389 377 378 372 366 369 354 364 342 361 330 357 318 355 305 372 292 388 280 405 268 421 256 439 244 453 231 470 219 487 207 505 195 511 179 511 167 510 155 511 143 511 131 511 119 511 107 511 95 511 83 511 72 511 60 511 48 511 36 512 24 512 12 506 2 494 2 482 2 470 2 457 2 445 2 433 3 421 2 410 2 398 3 386 2 374 2 362 2 350 2 338 2 325 3 313 3 301 4 290 4 277 4 266 3 254 3 242 3 230 3 218 3 205 3 193 4 181 4 169 4 158 4 146 4 134 5 122 5 110 5 98 4 86 4 74 4 62 4 49 4 37 4 25 4 13 4 1 4 U 5 190 D 17 190 29 190 41 190 53 190 65 190 77 190 89 190 101 190 113 190 125 189 137 189 149 189 161 189 173 189 185 189 197 189 209 153 221 116 233 78 245 41 265 14 277 51 289 87 301 124 313 162 325 188 337 189 349 189 361 189 373 189 385 189 397 189 409 189 421 189 433 189 444 189 456 189 467 189 479 189 491 189 503 189 U 315 182 D 311 171 306 159 303 147 299 136 296 123 292 111 287 99 285 87 280 75 277 63 272 51 269 39 265 27 262 15 U 256 6 D 252 18 249 30 245 42 242 55 238 67 233 79 230 90 225 102 222 114 218 126 214 138 211 150 206 162 203 174 199 186 U 256 380 D 240 392 222 404 205 416 189 427 173 439 156 451 140 463 123 476 116 489 128 489 140 489 152 489 164 489 176 488 188 488 200 488 212 487 224 487 236 487 248 488 259 487 271 487 283 487 295 487 306 487 319 487 331 487 343 488 355 487 367 487 379 487 391 487 U 396 482 D 380 470 363 458 345 445 328 434 311 421 294 409 278 397 262 385

def write_to_arduino():
    arduino.write(bytes(my_str, 'utf-8'))

    # while(not arduino.readable()):
    #     pass
    while (arduino.readable):
        print (f'recvd message {arduino.read_all()}')

write_to_arduino()
# arduino.write(bytes('q', 'utf-8'))

