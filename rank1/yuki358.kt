import java.util.*;

fun main(args: Array<String>) {
	val cin = Scanner(System.`in`)

	var a = cin.nextInt()
	var b = cin.nextInt()
	var c = cin.nextInt()
	var maxNum = intArrayOf(a, b, c).max()!!

	var res: Int = 0
	for(i in 1..maxNum) {
		var tarr = intArrayOf(a % i, b % i, c % i)
		if(tarr[0] == tarr[1] || tarr[1] == tarr[2] || tarr[2] == tarr[0]) {
			continue
		}
		if(tarr[1] == tarr.max()!! || tarr[1] == tarr.min()!!) {
			res++
		}
	}

	maxNum++
	var tarr = intArrayOf(a % maxNum, b % maxNum, c % maxNum)
	if(tarr[0] == tarr[1] || tarr[1] == tarr[2] || tarr[2] == tarr[0]) {
		println(res)
	} else {
		if(tarr[1] == tarr.max()!! || tarr[1] == tarr.min()!!) {
			println("INF")
		} else {
			println(res)
		}
	}
}