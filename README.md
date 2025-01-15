# 分析结果

将c标准库函数与windows(msvcrt ntdll ucrtbase),linux(glibc),mac(dylib)导出函数比较，对不支持的情况分析

文件说明

windows相关

* ntdll.spec <https://github.com/wine-mirror/wine/blob/master/dlls/ntdll/ntdll.spec>
* msvcrt.spec <https://github.com/wine-mirror/wine/blob/master/dlls/msvcrt/msvcrt.spec>
* cstdapi.txt <https://zh.cppreference.com/w/c/symbol_index>
* wingood.txt windows上通过msvcrt ntdll ucrtbase导出函数支持的函数
* winbad.txt windows上不支持的函数

linux相关

* linuxgood.txt linux上通过glibc导出函数支持的函数
* linuxbad.txt linux上不支持的函数
* list_symbols.zig [glibc-abi-tool](https://github.com/ziglang/glibc-abi-tool/blob/dbe4e76400dedb2723bd284ed64cae8a7fb08ed9/list_symbols.zig)
* abilists <https://github.com/ziglang/zig/blob/0.13.0/lib/libc/glibc/abilists>
* glibcabi.txt `zig run list_symbols.zig -- abilists > glibcabi.txt` zig@0.13.0

mac相关

* libSystem.tbd <https://github.com/ziglang/zig/blob/0.13.0/lib/libc/darwin/libSystem.tbd>
* macgood.txt mac上通过libsystem_c.dylib导出函数支持的函数
* macbad.txt mac上不支持的函数

其他说明:

* wine中spec文件的文档: <https://gitlab.winehq.org/wine/wine/-/wikis/Man-Pages/winebuild#spec-file-syntax>
* zig中abilists文件的文档: <https://github.com/ziglang/glibc-abi-tool/blob/dbe4e76400dedb2723bd284ed64cae8a7fb08ed9/README.md>

## linux不支持的情况

### inline的情况

```
at_quick_exit (C11 起) 调用了__cxa_at_quick_exit 
```

### atomic不支持

```
atomic_compare_exchange_strong (generic) (C11 起)
atomic_compare_exchange_strong_explicit (generic) (C11 起)
atomic_compare_exchange_weak (generic) (C11 起)
atomic_compare_exchange_weak_explicit (generic) (C11 起)
atomic_exchange (generic) (C11 起)
atomic_exchange_explicit (generic) (C11 起)
atomic_fetch_add (generic) (C11 起)
atomic_fetch_add_explicit (generic) (C11 起)
atomic_fetch_and (generic) (C11 起)
atomic_fetch_and_explicit (generic) (C11 起)
atomic_fetch_or (generic) (C11 起)
atomic_fetch_or_explicit (generic) (C11 起)
atomic_fetch_sub (generic) (C11 起)
atomic_fetch_sub_explicit (generic) (C11 起)
atomic_fetch_xor (generic) (C11 起)
atomic_fetch_xor_explicit (generic) (C11 起)
atomic_flag_clear (C11 起)
atomic_flag_clear_explicit (C11 起)
atomic_flag_test_and_set (C11 起)
atomic_flag_test_and_set_explicit (C11 起)
atomic_init (generic) (C11 起)
atomic_is_lock_free (generic) (C11 起)
atomic_load (generic) (C11 起)
atomic_load_explicit (generic) (C11 起)
atomic_signal_fence (C11 起)
atomic_store (generic) (C11 起)
atomic_store_explicit (generic) (C11 起)
atomic_thread_fence (C11 起)
```

### safe函数不支持

```
abort_handler_s (C11 起)
asctime_s (C11 起)
bsearch_s (C11 起)
ctime_s (C11 起)
fopen_s (C11 起)
fprintf_s (C11 起)
freopen_s (C11 起)
fscanf_s (C11 起)
fwprintf_s (C11 起)
fwscanf_s (C11 起)
getenv_s (C11 起)
gets_s (C11 起)
gmtime_s (C11 起)
ignore_handler_s (C11 起)
localtime_s (C11 起)
mbsrtowcs_s (C11 起)
mbstowcs_s (C11 起)
memcpy_s (C11 起)
memmove_s (C11 起)
memset_s (C11 起)
printf_s (C11 起)
qsort_s (C11 起)
scanf_s (C11 起)
set_constraint_handler_s (C11 起)
snprintf_s (C11 起)
snwprintf_s (C11 起)
sprintf_s (C11 起)
sscanf_s (C11 起)
strcat_s (C11 起)
strcpy_s (C11 起)
strerror_s (C11 起)
strerrorlen_s (C11 起)
strncat_s (C11 起)
strncpy_s (C11 起)
strnlen_s (C11 起)
strtok_s (C11 起)
swprintf_s (C11 起)
swscanf_s (C11 起)
tmpfile_s (C11 起)
tmpnam_s (C11 起)
vfprintf_s (C11 起)
vfscanf_s (C11 起)
vfwprintf_s (C11 起)
vfwscanf_s (C11 起)
vprintf_s (C11 起)
vscanf_s (C11 起)
vsnprintf_s (C11 起)
vsnwprintf_s (C11 起)
vsprintf_s (C11 起)
vsscanf_s (C11 起)
vswprintf_s (C11 起)
vswscanf_s (C11 起)
vwprintf_s (C11 起)
vwscanf_s (C11 起)
wcrtomb_s (C11 起)
wcscat_s (C11 起)
wcscpy_s (C11 起)
wcsncat_s (C11 起)
wcsncpy_s (C11 起)
wcsnlen_s (C11 起)
wcsrtombs_s (C11 起)
wcstok_s (C11 起)
wcstombs_s (C11 起)
wctomb_s (C11 起)
wmemcpy_s (C11 起)
wmemmove_s (C11 起)
wprintf_s (C11 起)
wscanf_s (C11 起)
```

### C23不支持的情况

```
memset_explicit (C23 起)
```

## windows不支持的情况

### C95不支持的情况

#### inline引起

```
fwide (C95 起)
mbsinit (C95 起)
wmemchr (C95 起)
wmemcmp (C95 起)
wmemcpy (C95 起)
wmemmove (C95 起)
wmemset (C95 起)
```

### C99不支持的情况

#### inline引起

```
hypotf (C99 起)  实际导出了 _hypotf
snprintf (C99 起) 实际导出了 _snprintf
ldexpf (C99 起) 调用了ldexp
vfscanf (C99 起) 最终调用了 __stdio_common_vfscanf
vfwscanf (C99 起) 最终调用了 __stdio_common_vfscanf
vscanf (C99 起) 最终调用了 __stdio_common_vfscanf
vsscanf (C99 起) 最终调用了 __stdio_common_vfscanf
vswscanf (C99 起) 最终调用了 __stdio_common_vfscanf
vwscanf (C99 起) 最终调用了 __stdio_common_vfscanf
feraiseexcept (C99 起)
feupdateenv (C99 起)
```

#### long double inline 类型引起

其实现都是将long double转为double, 在调用对应函数,如acosl -> acos

```
acosl (C99 起)
asinl (C99 起)
atan2l (C99 起)
atanl (C99 起)
ceill (C99 起)
coshl (C99 起)
cosl (C99 起)
expl (C99 起)
fabsl (C99 起)
floorl (C99 起)
fmodl (C99 起)
frexpl (C99 起)
hypotl (C99 起)
ldexpl (C99 起)
log10l (C99 起)
logl (C99 起)
modfl (C99 起)
powl (C99 起)
sinhl (C99 起)
sinl (C99 起)
sqrtl (C99 起)
tanhl (C99 起)
tanl (C99 起)
```

### C11不支持的情况

```
abort_handler_s (C11 起)
aligned_alloc (C11 起)
at_quick_exit (C11 起)
atomic_compare_exchange_strong (generic) (C11 起)
atomic_compare_exchange_strong_explicit (generic) (C11 起)
atomic_compare_exchange_weak (generic) (C11 起)
atomic_compare_exchange_weak_explicit (generic) (C11 起)
atomic_exchange (generic) (C11 起)
atomic_exchange_explicit (generic) (C11 起)
atomic_fetch_add (generic) (C11 起)
atomic_fetch_add_explicit (generic) (C11 起)
atomic_fetch_and (generic) (C11 起)
atomic_fetch_and_explicit (generic) (C11 起)
atomic_fetch_or (generic) (C11 起)
atomic_fetch_or_explicit (generic) (C11 起)
atomic_fetch_sub (generic) (C11 起)
atomic_fetch_sub_explicit (generic) (C11 起)
atomic_fetch_xor (generic) (C11 起)
atomic_fetch_xor_explicit (generic) (C11 起)
atomic_flag_clear (C11 起)
atomic_flag_clear_explicit (C11 起)
atomic_flag_test_and_set (C11 起)
atomic_flag_test_and_set_explicit (C11 起)
atomic_init (generic) (C11 起)
atomic_is_lock_free (generic) (C11 起)
atomic_load (generic) (C11 起)
atomic_load_explicit (generic) (C11 起)
atomic_signal_fence (C11 起)
atomic_store (generic) (C11 起)
atomic_store_explicit (generic) (C11 起)
atomic_thread_fence (C11 起)
call_once (C11 起)
cnd_broadcast (C11 起)
cnd_destroy (C11 起)
cnd_init (C11 起)
cnd_signal (C11 起)
cnd_timedwait (C11 起)
cnd_wait (C11 起)
ctime_s (C11 起)
gmtime_s (C11 起)
ignore_handler_s (C11 起)
localtime_s (C11 起)
memset_s (C11 起)
mtx_destroy (C11 起)
mtx_init (C11 起)
mtx_lock (C11 起)
mtx_timedlock (C11 起)
mtx_trylock (C11 起)
mtx_unlock (C11 起)
set_constraint_handler_s (C11 起)
snprintf_s (C11 起)
snwprintf_s (C11 起)
strerrorlen_s (C11 起)
strnlen_s (C11 起)
thrd_create (C11 起)
thrd_current (C11 起)
thrd_detach (C11 起)
thrd_equal (C11 起)
thrd_exit (C11 起)
thrd_join (C11 起)
thrd_sleep (C11 起)
thrd_yield (C11 起)
timespec_get (C11 起)
tss_create (C11 起)
tss_delete (C11 起)
tss_get (C11 起)
tss_set (C11 起)
vfscanf_s (C11 起)
vfwscanf_s (C11 起)
vscanf_s (C11 起)
vsnprintf_s (C11 起)
vsnwprintf_s (C11 起)
vsscanf_s (C11 起)
vswscanf_s (C11 起)
vwscanf_s (C11 起)
wcsnlen_s (C11 起)
```

### C23不支持的情况

```
gmtime_r (C23 起)
localtime_r (C23 起)
memccpy (C23 起)
memset_explicit (C23 起)
strdup (C23 起)
strndup (C23 起)
timespec_getres (C23 起)
```

## mac不支持的情况


### 不支持

```
at_quick_exit (C11 起)
tss_create (C11 起)
tss_delete (C11 起)
tss_get (C11 起)
tss_set (C11 起)
timespec_getres (C23 起)
thrd_create (C11 起)
thrd_current (C11 起)
thrd_detach (C11 起)
thrd_equal (C11 起)
thrd_exit (C11 起)
thrd_join (C11 起)
thrd_sleep (C11 起)
thrd_yield (C11 起)
quick_exit (C11 起)
memset_explicit (C23 起)
mbrtoc16 (C11 起)
mbrtoc32 (C11 起)
c16rtomb (C11 起)
c32rtomb (C11 起)
call_once (C11 起)
cnd_broadcast (C11 起)
cnd_destroy (C11 起)
cnd_init (C11 起)
cnd_signal (C11 起)
cnd_timedwait (C11 起)
cnd_wait (C11 起)
mtx_destroy (C11 起)
mtx_init (C11 起)
mtx_lock (C11 起)
mtx_timedlock (C11 起)
mtx_trylock (C11 起)
mtx_unlock (C11 起)
```

### safe 函数

```
abort_handler_s (C11 起)
asctime_s (C11 起)
bsearch_s (C11 起)
ctime_s (C11 起)
fopen_s (C11 起)
fprintf_s (C11 起)
freopen_s (C11 起)
fscanf_s (C11 起)
fwprintf_s (C11 起)
fwscanf_s (C11 起)
getenv_s (C11 起)
gets_s (C11 起)
gmtime_s (C11 起)
ignore_handler_s (C11 起)
localtime_s (C11 起)
mbsrtowcs_s (C11 起)
mbstowcs_s (C11 起)
memcpy_s (C11 起)
memmove_s (C11 起)
printf_s (C11 起)
qsort_s (C11 起)
scanf_s (C11 起)
set_constraint_handler_s (C11 起)
snprintf_s (C11 起)
snwprintf_s (C11 起)
sprintf_s (C11 起)
sscanf_s (C11 起)
strcat_s (C11 起)
strcpy_s (C11 起)
strerror_s (C11 起)
strerrorlen_s (C11 起)
strncat_s (C11 起)
strncpy_s (C11 起)
strnlen_s (C11 起)
strtok_s (C11 起)
swprintf_s (C11 起)
swscanf_s (C11 起)
tmpfile_s (C11 起)
tmpnam_s (C11 起)
vfprintf_s (C11 起)
vfscanf_s (C11 起)
vfwprintf_s (C11 起)
vfwscanf_s (C11 起)
vprintf_s (C11 起)
vscanf_s (C11 起)
vsnprintf_s (C11 起)
vsnwprintf_s (C11 起)
vsprintf_s (C11 起)
vsscanf_s (C11 起)
vswprintf_s (C11 起)
vswscanf_s (C11 起)
vwprintf_s (C11 起)
vwscanf_s (C11 起)
wcrtomb_s (C11 起)
wcscat_s (C11 起)
wcscpy_s (C11 起)
wcsncat_s (C11 起)
wcsncpy_s (C11 起)
wcsnlen_s (C11 起)
wcsrtombs_s (C11 起)
wcstok_s (C11 起)
wcstombs_s (C11 起)
wctomb_s (C11 起)
wmemcpy_s (C11 起)
wmemmove_s (C11 起)
wprintf_s (C11 起)
wscanf_s (C11 起)
```

### 原子操作

```
atomic_compare_exchange_strong (generic) (C11 起)
atomic_compare_exchange_strong_explicit (generic) (C11 起)
atomic_compare_exchange_weak (generic) (C11 起)
atomic_compare_exchange_weak_explicit (generic) (C11 起)
atomic_exchange (generic) (C11 起)
atomic_exchange_explicit (generic) (C11 起)
atomic_fetch_add (generic) (C11 起)
atomic_fetch_add_explicit (generic) (C11 起)
atomic_fetch_and (generic) (C11 起)
atomic_fetch_and_explicit (generic) (C11 起)
atomic_fetch_or (generic) (C11 起)
atomic_fetch_or_explicit (generic) (C11 起)
atomic_fetch_sub (generic) (C11 起)
atomic_fetch_sub_explicit (generic) (C11 起)
atomic_fetch_xor (generic) (C11 起)
atomic_fetch_xor_explicit (generic) (C11 起)
atomic_init (generic) (C11 起)
atomic_is_lock_free (generic) (C11 起)
atomic_load (generic) (C11 起)
atomic_load_explicit (generic) (C11 起)
atomic_store (generic) (C11 起)
atomic_store_explicit (generic) (C11 起)
```