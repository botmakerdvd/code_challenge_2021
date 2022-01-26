#!/usr/bin/python3
T={
  'Ab' : 'Bb',
  'A'  : 'B',
  'A#' : 'B#',
  'Bb' : 'C',
  'B' :  'C#',
  'B#' : 'error',
  'Cb' : 'Db',
  'C'  : 'D',
  'C#' : 'D#',
  'Db' : 'Eb',
  'D'  : 'E',
  'D#' : 'E#',
  'Eb' : 'F',
  'E'  : 'F#',
  'E#' : 'error',
  'Fb' : 'Gb',
  'F'  : 'G',
  'F#' : 'G#',
  'Gb' : 'Ab',
  'G'  : 'A',
  'G#' : 'A#'
}
s={
  'Ab' : 'error',
  'A'  : 'Bb',
  'A#' : 'B',
  'Bb' : 'Cb',
  'B' :  'C',
  'B#' : 'C#',
  'Cb' : 'error',
  'C'  : 'Db',
  'C#' : 'D',
  'Db' : 'error',
  'D'  : 'Eb',
  'D#' : 'E',
  'Eb' : 'Fb',
  'E'  : 'F',
  'E#' : 'F#',
  'Fb' : 'error',
  'F'  : 'Gb',
  'F#' : 'G',
  'Gb' : 'error',
  'G'  : 'Ab',
  'G#' : 'A'
}
n = int(input())
for case in range(n):
	start=input()
	scale=input()
	currentletter=start
	print("Case #"+str(case+1)+": ", end="")
	for i in range(7):
		print(currentletter, end ="")
		if scale[i] == 'T':
			currentletter=T[currentletter]
		else:
			currentletter=s[currentletter]	
	print(currentletter) 