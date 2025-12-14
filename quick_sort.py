# File: quick_sort.py

# List global untuk menyimpan riwayat langkah
HISTORY = []

def quick_sort(data_list):
    """
    Mengimplementasikan Quick Sort dan mencatat riwayat langkah yang konsisten.
    """
    global HISTORY
    HISTORY = []
    
    # Buat salinan array yang akan diurutkan.
    data_to_sort = data_list[:] 
    
    _quick_sort_recursive(data_to_sort, 0, len(data_to_sort) - 1)
    
    # Tambahkan state terakhir (selesai)
    # Highlight: 4 elemen konsisten (-1, -1, -1, 'Selesai')
    HISTORY.append({'array': data_to_sort[:], 'highlight': (-1, -1, -1, 'Selesai'), 'action': 'Pengurutan Selesai'})
    
    return data_to_sort, HISTORY

def _quick_sort_recursive(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        
        # Rekursif
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)

def _partition(arr, low, high):
    
    pivot = arr[high] # Pivot adalah elemen terakhir
    i = low - 1  # Indeks elemen yang lebih kecil

    # Catat state saat memilih Pivot
    HISTORY.append({
        'array': arr[:],
        # Highlight: (low, high, index_pivot, status_aksi)
        'highlight': (low, high, high, 'Pilih Pivot'), 
        'action': f'Memulai Partisi: Rentang [{low}-{high}]. Pivot: {pivot} di Indeks {high}'
    })
    
    for j in range(low, high):
        
        # Catat state saat Membandingkan
        HISTORY.append({
            'array': arr[:],
            # J: Elemen yang dibandingkan, High: Pivot
            'highlight': (low, high, j, 'Bandingkan'), 
            'action': f'Bandingkan Indeks {j} ({arr[j]}) dengan Pivot {pivot}'
        })
        
        if arr[j] <= pivot:
            
            i = i + 1
            
            # Tukar arr[i] dan arr[j] jika i != j
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
                
                # Catat state setelah Penukaran
                HISTORY.append({
                    'array': arr[:],
                    # i dan j: Elemen yang baru saja ditukar
                    'highlight': (low, high, i, 'Tukar'), 
                    'action': f'Tukar {arr[j]} (Indeks {j}) dengan {arr[i]} (Indeks {i})'
                })
            
    # Akhir: Tukar pivot (arr[high]) dengan elemen di posisi i+1
    if i + 1 != high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Catat state setelah Pivot ditempatkan di posisi akhir
    HISTORY.append({
        'array': arr[:],
        'highlight': (low, high, i + 1, 'Pivot Final'), 
        'action': f'Pivot {pivot} ditempatkan di posisi akhirnya: Indeks {i + 1}'
    })
    
    return i + 1
