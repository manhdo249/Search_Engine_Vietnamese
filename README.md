# Search Engine Vietnamese

**Search Engine Vietnamese** là một công cụ tìm kiếm được thiết kế đặc biệt để phục vụ người dùng Việt Nam, tối ưu hóa trải nghiệm tìm kiếm bằng tiếng Việt. Dự án này nhằm giúp người dùng tìm kiếm thông tin nhanh chóng và chính xác từ nhiều nguồn dữ liệu đa dạng trong ngữ cảnh văn hóa và ngôn ngữ Việt.

## I. Mục tiêu của dự án

- Tối ưu hóa tìm kiếm cho tiếng Việt, với khả năng xử lý ngôn ngữ tự nhiên và truy vấn bằng tiếng Việt.
- Cung cấp kết quả tìm kiếm phù hợp với ngữ cảnh văn hóa và nhu cầu thông tin của người Việt.

## II. Tính năng

- **Xử lý ngôn ngữ tự nhiên**: Hỗ trợ các truy vấn tiếng Việt, bao gồm từ đồng nghĩa, từ viết tắt, và các dạng từ đa nghĩa.
- **Tìm kiếm theo ngữ cảnh**: Hiển thị kết quả tìm kiếm phù hợp với bối cảnh văn hóa, địa lý và ngôn ngữ của Việt Nam.
- **Lọc và sắp xếp kết quả**: Người dùng có thể lọc kết quả theo tiêu chí điểm số từ cao xuống thấp.
- **<Sắp update>**
  - **Đề xuất tự động**: Đề xuất các cụm từ liên quan và gợi ý truy vấn tiếp theo giúp người dùng dễ dàng tìm thấy thông tin.
  - **Giao diện thân thiện với người dùng**: Thiết kế tối giản, dễ sử dụng cho mọi lứa tuổi, từ người mới bắt đầu đến người dùng chuyên nghiệp.

## III. Cấu trúc dự án

```plaintext
SearchEngineVietnamese/
├── TF-IDF_SparseMatrix.py                     
├── docs.json                   
├── ds.json                      
├── tf_idf_list.json               
├── vietnamese-stopwords.txt                
├── rawSearch.py                # Search thô
├── reranker.py                 # Search vector
├── serve.py                    # Deploy 
├── README.md                   # Tài liệu hướng dẫn sử dụng
└── requirements.txt            # Danh sách thư viện cần cài đặt
```

## IV. Kiến trúc hệ thống Search Engine Vietnamese

Dưới đây là sơ đồ kiến trúc tổng thể của hệ thống **Search Engine Vietnamese**. Sơ đồ này mô tả các thành phần chính của hệ thống và cách chúng tương tác với nhau để cung cấp khả năng tìm kiếm thông tin tối ưu cho người dùng Việt Nam.

![Kiến trúc hệ thống SearchEngineVietnamese](https://i.imgur.com/hPEHoZc.jpeg)

## V. Demo Triển Khai API

![Watch the video](https://i.imgur.com/QYwlnk5.jpeg)


