// #include <parallel/parallel.h>

// #include <algorithm>
// #include <future>
// #include <iostream>
// #include <numeric>
// #include <thread>
// #include <functional>
// #include <vector>

// using namespace concurrency;

// template <typename RAIter>
// int parallel_sum(RAIter beg, RAIter end) {
//     auto len = end - beg;
//     if (len < 1000)
//         return std::accumulate(beg, end, 0);

//     RAIter mid = beg + len / 2;
//     auto handle = std::async(std::launch::async,
//                              parallel_sum<RAIter>, mid, end);
//     int sum = parallel_sum(beg, mid);
//     return sum + handle.get();
// }

// /// Basically replacing:
// void sequential_for() {
//     for (int i = 0; i < 1000; ++i)
//         std::cout << "Stuff";
// }

// /// By:
// void threaded_for() {
//     parallel_for(1000, [&](int start, int end) {
//         for (int i = start; i < end; ++i)
//             std::cout << "Stuff";
//     });
// }

// int main() {
//     // std::vector<int> v(10000, 1);
//     // std::cout << "The sum is " << parallel_sum(v.begin(), v.end()) << '\n';
// }

#include <algorithm>
#include <functional>
#include <thread>
#include <vector>

/// @param[in] nb_elements : size of your for loop
/// @param[in] functor(start, end) :
/// your function processing a sub chunk of the for loop.
/// "start" is the first index to process (included) until the index "end"
/// (excluded)
/// @code
///     for(int i = start; i < end; ++i)
///         computation(i);
/// @endcode
/// @param use_threads : enable / disable threads.
///
///
static void parallel_for(unsigned nb_elements,
                         std::function<void(int start, int end)> functor,
                         bool use_threads = true) {
    // -------
    unsigned nb_threads_hint = std::thread::hardware_concurrency();
    unsigned nb_threads = nb_threads_hint == 0 ? 8 : (nb_threads_hint);

    unsigned batch_size = nb_elements / nb_threads;
    unsigned batch_remainder = nb_elements % nb_threads;

    std::vector<std::thread> my_threads(nb_threads);

    if (use_threads) {
        // Multithread execution
        for (unsigned i = 0; i < nb_threads; ++i) {
            int start = i * batch_size;
            my_threads[i] = std::thread(functor, start, start + batch_size);
        }
    } else {
        // Single thread execution (for easy debugging)
        for (unsigned i = 0; i < nb_threads; ++i) {
            int start = i * batch_size;
            functor(start, start + batch_size);
        }
    }

    // Deform the elements left
    int start = nb_threads * batch_size;
    functor(start, start + batch_remainder);

    // Wait for the other thread to finish their task
    if (use_threads)
        std::for_each(my_threads.begin(), my_threads.end(), std::mem_fn(&std::thread::join));
}