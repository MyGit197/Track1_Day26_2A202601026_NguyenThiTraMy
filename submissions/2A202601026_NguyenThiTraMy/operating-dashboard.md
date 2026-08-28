# Operating Dashboard — LinguaFlow AI

> Đây là **worksheet nguồn** để validator và rubric truy vết evidence. Sau khi
> hoàn tất, rút gọn phần vận hành sang
> `templates/one-page-dashboard-template.md`; không ép bảng 12 cột này lên một trang.

- Học viên: Nguyễn Thị Trà My
- Mã học viên: 2A202601026
- Mô hình: B2B
- Cập nhật: 2026-08-28
- North Star: Median Time-to-first-value dưới 7 ngày

## Chẩn đoán mô hình

LinguaFlow AI là sản phẩm B2B vì doanh nghiệp (công ty IT Outsourcing & Xuất nhập khẩu quy mô 20–200 nhân sự) trả tiền mua gói cho đội ngũ dự án, người dùng trực tiếp là PM và nhân sự nội bộ vận hành cuộc họp đa quốc gia, sản phẩm không có quan hệ độc lập với khách hàng cuối của doanh nghiệp.

| Dữ liệu đầu vào | Trạng thái | Nằm ở đâu hoặc cần gì để đo | Ngày có số |
|---|---|---|---|
| Unit economics Day 24 | Đo được | File mô hình tài chính 2A202601026_NguyenThiTraMy_Day25_model.xlsx đã loại dữ liệu khách hàng | 2026-08-28 |
| Value Metric và Cost/Job Day 25 | Đo được | Báo cáo Cost/Job $0.4102 per completed meeting trong evidence pack | 2026-08-28 |

## Kiểm kê đèn ứng viên

| Đèn ứng viên từ handbook | Tầng | Trạng thái | Bằng chứng hiện có hoặc kế hoạch đo |
|---|---|---|---|
| Time-to-first-value (TTFV) | L | ✅ | Event kickoff và milestone xuất task tự động đã được ghi log trong hệ thống |
| Pipeline coverage | L | 🔧 | Chuẩn hóa cơ hội từ Partner trong CRM trước ngày 2026-09-10 |
| % deal chết ở khâu security/procurement | L | 🔧 | Thêm trường lý do thất bại bắt buộc trong CRM trước ngày 2026-09-10 |
| POC → paid | O | ✅ | Dữ liệu cohort 10 doanh nghiệp pilot đầu tiên |
| Sales cycle (ngày) | O | 🔧 | Ghi nhận ngày qualified deal cho các khách hàng Partner giới thiệu trước 2026-09-15 |
| Usage depth trong tài khoản | O | ✅ | Số lượng cuộc họp hàng tuần theo từng tài khoản trong event log |
| Chi phí triển khai ÷ ACV | O | 🔧 | Gắn timesheet hỗ trợ kỹ thuật với hợp đồng Partner trước 2026-09-15 |
| Tập trung doanh thu | O | ✅ | Báo cáo doanh thu theo danh mục khách hàng đã redacted |
| NRR | G | 🔧 | Theo dõi cohort doanh nghiệp sau 2 quý vào 2027-02-28 |
| Gross Margin | G | ✅ | Báo cáo tài chính ghép chi phí API LLM, Speech và HITL |
| CAC payback | G | 🔧 | Chuẩn hóa fully-loaded CAC bao gồm hoa hồng Partner trước 2026-10-15 |

## Đèn báo sớm

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| L-01 | Time-to-first-value | Số ngày từ kickoff đến cuộc họp đa quốc gia đầu tiên xuất biên bản đạt QA; median theo cohort | Tuần · Product Operations | 14 ngày | ≤7 ngày | 8–14 ngày | >14 ngày | [TB] Đo 3 cohort pilot ban đầu để chốt baseline chính thức vào ngày 2026-10-31 | 2026-08-28 | POC-to-paid và NRR | R-01 |
| L-02 | Pipeline coverage qua Partner | Tổng ARR pipeline xác minh bởi Partner chia cho target doanh thu quý | Tuần · Revenue Operations | 2.4× | ≥3.0× | 2.0–2.9× | <2.0× | [TB] Áp dụng quy ước ngành 3.0× cho win rate 33%, sẽ điều chỉnh vào 2026-11-30 | 2026-08-28 | POC-to-paid | R-02 |

## Đèn vận hành

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| O-01 | Containment Rate | Số cuộc họp hoàn thành tự động không lỗi chia tổng cuộc họp khởi tạo AI | Tuần · Product Operations | 82.0% | ≥80.0% | 71.63–79.9% | <71.63% | [MH] MH-02 suy từ mô hình hòa vốn Gross Margin 60% | 2026-08-28 | Gross Margin | R-03 |
| O-02 | Chi phí AI & Speech trên mỗi completed job | Tổng chi phí API LLM, Speech, TTS và Retry chia số cuộc họp hoàn thành đạt QA | Tuần · FinOps | $0.159 | ≤$0.200 | $0.201–$0.423 | >$0.423 | [MH] MH-01 suy từ unit economics Day 25 để đảm bảo Gross Margin ≥ 60% | 2026-08-28 | Gross Margin | R-04 |
| O-03 | POC → paid conversion | Số doanh nghiệp pilot ký paid chính thức chia tổng doanh nghiệp kết thúc pilot | Tháng · Revenue Operations | 40.0% | ≥50.0% | 35.0–49.9% | <35.0% | [BM] Benchmarkit State of B2B SaaS 2026 https://www.benchmarkit.ai/reports/2026-b2b-saas-benchmarks mốc trung vị conversion POC/pilot B2B là ~50.0% | 2026-08-28 | CAC payback | R-03 |

## Đèn kết quả

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| G-01 | Gross margin sau chi phí AI & HITL | (Doanh thu - tổng COGS gồm LLM, Speech, Infra, QA và Escalation) chia doanh thu | Tháng · Finance | 72.65% | ≥60.0% | 50.0–59.9% | <50.0% | [BM] ICONIQ Growth AI Cloud Report 2026 https://www.iconiqgrowth.com/insights/ai-cloud-2026 biên lợi nhuận gộp trung vị AI-native SaaS 2026E là ~53.0%, đặt mục tiêu an toàn ≥ 60.0% | 2026-08-28 | Runway và Payback | R-04 |
| G-02 | CAC Payback Period | Fully-loaded CAC gồm 25% rev-share Partner chia (ARPU tháng × Gross Margin %) | Quý · Finance | 8.5 tháng | ≤12.0 tháng | 12.1–15.0 tháng | >15.0 tháng | [BM] Bessemer Venture Partners State of the Cloud 2026 https://www.bvp.com/atlas/state-of-the-cloud-2026 mốc an toàn SMB B2B SaaS payback < 12 tháng | 2026-08-28 | LTV/CAC | R-05 |

## Luật quyết định

| ID | NẾU | TRONG | VÀ | THÌ | KHÔNG THÌ | Luật dừng? |
|---|---|---|---|---|---|---|
| R-01 | Median TTFV > 14 ngày | 2 cohort liên tiếp | Có ít nhất 5 doanh nghiệp pilot trong mỗi cohort | Tạm dừng nhận pilot mới trong 14 ngày và cắt giảm quy trình onboarding xuống 1 use case cuộc họp Google Meet duy nhất | Không giảm giá hợp đồng để bù đắp cho việc triển khai chậm | CÓ |
| R-02 | Pipeline coverage qua Partner < 2.0× | 3 tuần liên tiếp | Có ít nhất 3 Partner đang ký hợp tác phân phối | Điều chuyển 1 nhân sự Partner Enablement sang hỗ trợ trực tiếp các buổi demo bán hàng cùng Partner | Không tự mở rộng kênh bán Outbound trực tiếp gây xung đột với Partner | KHÔNG |
| R-03 | Containment Rate < 71.63% | 2 tuần liên tiếp | Có ít nhất 100 cuộc họp được khởi tạo qua AI bot | Đóng băng toàn bộ hoạt động Outbound sales và tập trung 100% nguồn lực engineering tinh chỉnh prompt dịch thuật trong 1 sprint | Không tăng ngân sách Marketing để tuyển thêm POC nhằm lấp liếm tỷ lệ chuyển đổi kém | CÓ |
| R-04 | Chi phí AI & Speech > $0.423 / completed job | 2 tuần liên tiếp | Có ít nhất 200 cuộc họp hoàn thành đạt chuẩn | Kích hoạt cơ chế Semantic Caching, cắt giảm context window từ 6 turns xuống 3 turns và đàm phán lại giá sỉ với Deepgram | Không cắt bỏ quy trình QA nội bộ 5% để làm đẹp con số chi phí | KHÔNG |
| R-05 | CAC Payback > 15.0 tháng | 2 quý liên tiếp | Có ít nhất 15 doanh nghiệp trả phí | Tái đàm phán giảm tỷ lệ hoa hồng Partner từ 25% xuống 18% và tập trung upsell gói dung lượng cho khách hàng hiện hữu | Không chi thêm ngân sách khuyến mãi tài trợ trải nghiệm miễn phí cho khách hàng mới | KHÔNG |

## Cổng gác 90 ngày

| Ngày | Metric gác cổng | Ngưỡng | Bằng chứng vật lý | Nếu đạt | Nếu trượt |
|---:|---|---|---|---|---|
| 30 | Tỷ lệ doanh nghiệp pilot hoàn thành 5 cuộc họp thật đầu tiên trong 14 ngày | ≥70.0% trên 10 doanh nghiệp pilot | Báo cáo Event log từ Google Meet Chrome Extension đã redacted | GO | FIX |
| 60 | Median Time-to-first-value (TTFV) | ≤7.0 ngày trên ít nhất 15 doanh nghiệp pilot | Báo cáo TTFV Cohort từ hệ thống Product Analytics | GO | PIVOT |
| 90 | Gross Margin sau chi phí AI & HITL | ≥60.0% trên ít nhất 35 doanh nghiệp trả phí | Báo cáo Billing export ghép với chi phí API LLM & Speech | GO | KILL |

## Kill criteria

Tuyên bố KILL và dừng toàn bộ dự án LinguaFlow AI vào ngày 90 nếu Gross Margin sau chi phí AI & HITL vẫn dưới 50.0% sau 2 sprint tối ưu prompt/model và không đạt tối thiểu 20 doanh nghiệp trả phí chấp nhận mức giá $1.50/completed meeting.

## Chưa đo được

| Đèn hoặc giả định | Cần gì để đo | Ai chịu trách nhiệm | Ngày có số |
|---|---|---|---|
| Tỷ lệ lỗi dịch thuật do tiếng lóng ngành IT/Logistics trong các cuộc họp thoại thực tế | Thu thập 50 mẫu audio cuộc họp thử nghiệm có sự đồng ý của khách hàng và đánh giá Eval theo bộ tiêu chuẩn Day 21-22 | Product Operations Lead | 2026-09-15 |

## Phụ lục ngưỡng suy từ mô hình

| ID | Metric | Input Day 24–25 | Phép tính | Kết quả và ngưỡng áp dụng |
|---|---|---|---|---|
| MH-01 | Chi phí AI & Speech tối đa trên mỗi completed job | Giá bán P = $1.50/job; GM mục tiêu = 60%; Chi phí QA q = $0.015/job; Chi phí Escalation e = $0.90/ca với tỷ lệ lỗi 18% (tương đương $0.162/job) | 1.50 x (1 - 0.60) - 0.015 - 0.162 = 0.423 | Chi phí AI tối đa cho phép là $0.423/job. Áp dụng cho ngưỡng Đỏ của O-02 (>$0.423) và G-01 (<60%) |
| MH-02 | Tỷ lệ Containment Rate tối thiểu để đạt hòa vốn GM mục tiêu | Giá P = $1.50/job; Biến phí v = $0.15939; QA q = $0.01500; Escalation e = $0.90000; GM mục tiêu = 60% | (0.15939 + 0.01500 + 0.90000) / (1.50 x 0.40 + 0.90000) = 1.07439 / 1.50000 = 71.63% | Tỷ lệ Containment Rate tối thiểu phải đạt 71.63%. Áp dụng cho ngưỡng Đỏ của O-01 (<71.63%) |

## Ghi nhận AI critique

| Phản biện | Chấp nhận hay bác bỏ | Thay đổi đã thực hiện | Lý do |
|---|---|---|---|
| TTFV cần định nghĩa kết quả đo lường cụ thể thay vì chỉ cài xong bot | Chấp nhận | Bổ sung mốc hoàn thành cuộc họp đa quốc gia đầu tiên đạt 100% QA và tự động xuất task sang Slack/Notion | Đảm bảo tính đo lường chính xác và không bị đọc thành cài đặt phần mềm thuần túy |
| Nên lấy benchmark NRR 101% của SaaS làm ngưỡng hành động | Bác bỏ | Giữ CAC Payback < 12 tháng và NRR đo theo cohort nội bộ | Giai đoạn 90 ngày đầu ưu tiên hoàn vốn CAC hơn mở rộng tài khoản NRR khi chưa đủ chu kỳ năm |
