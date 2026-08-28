# Operating Dashboard — LinguaFlow AI

> Bản rút gọn để xuất trang 1 PDF. Mọi giá trị phải khớp worksheet nguồn; chi
> tiết nguồn và hai phép tính `[MH]` nằm ở phụ lục trang 2.

**Model:** B2B · **Cập nhật:** 2026-08-28 · **Owner phiên họp:** Product Operations

**Chẩn đoán:** Doanh nghiệp trả phí theo gói/job; đội ngũ dự án (PM/Operations) vận hành cuộc họp đa quốc gia; sản phẩm không có quan hệ độc lập trực tiếp với khách hàng cuối của doanh nghiệp.

**North Star:** Median Time-to-first-value · hiện tại 14 ngày · mục tiêu ≤7 ngày · 🟡

## Cây đèn 3 tầng

| Tầng · ID | Metric và định nghĩa ngắn | Hiện tại · 🟢 / 🟡 / 🔴 · Nguồn | Nhịp · Owner | Báo trước cho · Luật |
|---|---|---|---|---|
| L · L-01 | Median ngày kickoff → cuộc họp đa quốc gia xuất biên bản QA | 14d · ≤7 / 8–14 / >14 · `[TB]` | Tuần · Product Ops | POC→paid + NRR · R-01 |
| L · L-02 | ARR pipeline từ Partner ÷ target doanh thu quý | 2.4× · ≥3.0 / 2.0–2.9 / <2.0 · `[TB]` | Tuần · Revenue Ops | POC→paid · R-02 |
| O · O-01 | Cuộc họp AI tự động hoàn thành ÷ tổng cuộc họp AI | 82.0% · ≥80.0 / 71.63–79.9 / <71.63 · `[MH]` | Tuần · Product Ops | Gross Margin · R-03 |
| O · O-02 | Chi phí API LLM, Speech & Retry ÷ completed meeting | $0.159 · ≤$0.200 / 0.201–0.423 / >0.423 · `[MH]` | Tuần · FinOps | Gross Margin · R-04 |
| O · O-03 | Pilot ký paid chính thức ÷ pilot kết thúc | 40.0% · ≥50.0 / 35.0–49.9 / <35.0 · `[BM]` | Tháng · Revenue Ops | CAC payback · R-03 |
| G · G-01 | (Doanh thu - tổng COGS) ÷ doanh thu | 72.65% · ≥60.0 / 50.0–59.9 / <50.0 · `[BM]` | Tháng · Finance | Runway + Payback · R-04 |
| G · G-02 | Fully-loaded CAC ÷ (ARPU tháng × GM %) | 8.5m · ≤12.0 / 12.1–15.0 / >15.0 · `[BM]` | Quý · Finance | LTV/CAC · R-05 |

## Luật quyết định

| ID | NẾU · TRONG · VÀ | THÌ | KHÔNG THÌ | Dừng? |
|---|---|---|---|---|
| R-01 | TTFV >14d · 2 cohort · ≥5 pilot/cohort | Tạm dừng pilot mới 14d; cắt onboarding xuống 1 use case Google Meet | Không giảm giá hợp đồng bù TTFV | CÓ |
| R-02 | Pipeline Partner <2.0× · 3 tuần · ≥3 Partner | Điều chuyển 1 Partner Enablement hỗ trợ demo trực tiếp | Không mở kênh Outbound trực tiếp | KHÔNG |
| R-03 | Containment <71.63% · 2 tuần · ≥100 cuộc họp | Đóng băng Outbound sales; dồn engineering sửa prompt 1 sprint | Không tăng MKT để tuyển thêm POC | CÓ |
| R-04 | Chi phí AI >$0.423/job · 2 tuần · ≥200 job QA | Kích hoạt Semantic Caching; giảm context window từ 6 về 3 turns | Không cắt bỏ quy trình QA 5% | KHÔNG |
| R-05 | CAC Payback >15.0m · 2 quý · ≥15 account paid | Tái đàm phán giảm rev-share Partner từ 25% về 18% và upsell | Không tài trợ khuyến mãi free khách mới | KHÔNG |

## Cổng 90 ngày

| Ngày | Một metric · ngưỡng | Evidence | Đạt / Trượt |
|---:|---|---|---|
| 30 | Tỷ lệ pilot xong 5 họp thật trong 14d · ≥70.0% trên 10 pilot | Event log report Google Meet redacted | GO / FIX |
| 60 | Median TTFV · ≤7.0d trên ≥15 pilot | Cohort report hệ thống Analytics | GO / PIVOT |
| 90 | Gross Margin sau AI & HITL · ≥60.0% trên ≥35 account | Billing export ghép chi phí API | GO / KILL |

**Kill criteria:** KILL ngày 90 nếu GM <50.0% sau 2 sprint tối ưu prompt/model và không có 20 account paid chấp nhận giá $1.50/job.

**Chưa đo được:** Tỷ lệ lỗi dịch tiếng lóng IT/Logistics · cần 50 mẫu audio và Eval Day 21-22 · owner Product Operations · có số 2026-09-15.
