read a;read b;read c;d=$[a/b];e=$[a/c];[ $[a%b] -eq 0 ] && d=$[d] || d=$[d+1];[ $[a%c] -eq 0 ] && e=$[e] || e=$[e+1];[ $[d*2-e*3] -ge 0 ] && echo YES || echo NO