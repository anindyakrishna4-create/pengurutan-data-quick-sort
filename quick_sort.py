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
    
    # Panggil fungsi rekursif utama
    _quick_sort_recursive(data_to_sort, 0, len(data_to_sort) - 1)
    
    # Tambahkan state terakhir (selesai)
    # Highlight: 4 elemen konsisten (-1, -1, -1, 'Selesai')
    HISTORY.append({'array': data_to_sort[:], 'highlight': (-1, -1, -1, 'Selesai'), 'action': 'Pengurutan Selesai'})
    
    # Kembalikan array yang sudah terurut.
    return data_to_sort, HISTORY

def _quick_sort_recursive(arr, low, high):
    if low < high:
        # Panggil fungsi partisi, yang mengembalikan indeks pivot
        pi = _partition(arr, low, high)
        
        # Rekursif pada sub-array di kiri pivot
        _quick_sort_recursive(arr, low, pi - 1)
        
        # Rekursif pada sub-array di kanan pivot
        _quick_sort_recursive(arr, pi + 1, high)

def _partition(arr, low, high):
    # Pilih elemen terakhir sebagai Pivot
    pivot = arr[high]
    i = low - 1  # Indeks elemen yang lebih kecil

    # Catat state saat memilih Pivot
    # Highlight: (low, high, index_pivot, status_aksi)
    HISTORY.append({
        'array': arr[:],
        'highlight': (low, high, high, 'Pilih Pivot'), 
        'action': f'Memulai Partisi: Rentang [{low}-{high}]. Pivot: {pivot} di Indeks {high}'
    })
    
    # Loop melalui elemen dari low hingga high-1
    for j in range(low, high):
        
        # Catat state saat Membandingkan. HIGHLIGHT INDEX J (elemen yang dibandingkan)
        HISTORY.append({
            'array': arr[:],
            'highlight': (low, high, j, 'Bandingkan'), # J: Elemen yang dibandingkan
            'action': f'Bandingkan Indeks {j} ({arr[j]}) dengan Pivot {pivot}'
        })
        
        # Jika elemen saat ini lebih kecil atau sama dengan pivot
        if arr[j] <= pivot:
            
            i = i + 1
            
            # Tukar arr[i] dan arr[j]
            arr[i], arr[j] = arr[j], arr[i]
            
            # Catat state setelah Penukaran. HIGHLIGHT INDEX I (yang menerima)
            HISTORY.append({
                'array': arr[:],
                'highlight': (low, high, i, 'Tukar'), # I: Elemen yang baru saja ditukar
                'action': f'Tukar {arr[j]} (Indeks {j}) dengan {arr[i]} (Indeks {i})'
            })
            
    # Tukar pivot (arr[high]) dengan elemen di posisi i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Catat state setelah Pivot ditempatkan di posisi akhir
    HISTORY.append({
        'array': arr[:],
        'highlight': (low, high, i + 1, 'Pivot Final'), # i+1 adalah posisi final Pivot
        'action': f'Pivot {pivot} ditempatkan di posisi akhirnya: Indeks {i + 1}'
    })
    
    # Kembalikan indeks tempat pivot berada
    return i + 1
