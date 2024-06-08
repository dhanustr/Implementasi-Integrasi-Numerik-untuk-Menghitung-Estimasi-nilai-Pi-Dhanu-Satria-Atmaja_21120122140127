import time
import numpy as np
import csv


# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Fungsi untuk menghitung integral menggunakan metode Riemann
def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    integral = 0.0
    for i in range(N):
        integral += f(a + i * dx) * dx
    return integral

# Fungsi untuk menghitung galat RMS
def rms_error(approx, exact):
    return np.sqrt((approx - exact) ** 2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Hasil pengukuran
results = []

for N in N_values:
    start_time = time.time()
    approx_pi = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    error = rms_error(approx_pi, pi_reference)
    execution_time = end_time - start_time
    
    results.append((N, approx_pi, error, execution_time))

# Cetak hasil
for result in results:
    N, approx_pi, error, execution_time = result
    print(f"N = {N}: approx_pi = {approx_pi}, error = {error}, execution_time = {execution_time} seconds")
with open('riemann_integral_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['N', 'approx_pi', 'error', 'execution_time'])
    for result in results:
        writer.writerow(result)

print("Results saved to riemann_integral_results.csv")