// 將整個程式碼包裝在一個函數中以避免變數重複宣告
function extractAndSortElements() {
    // 選擇所有符合條件的 <a> 元素
    const elements = document.querySelectorAll('a.card-shadow.rounded-lg');

    // 創建一個數組來存儲結果
    const results = [];

    // 遍歷每個元素並提取所需的信息
    elements.forEach(element => {
        const h3Text = element.querySelector('h3.mb-1').innerText;
        let timeText = element.querySelector('div.time.mb-1').innerText;
        const hrefLink = element.getAttribute('href');
        
        // 刪除 "Valid through" 和空白字串
        timeText = timeText.replace(/Valid through|^\s*|\s*$/g, '').trim();
        
        // 以 "~" 符號切割日期
        const dates = timeText.split('~').map(date => date.trim());
        
        // 檢查是否有兩個有效的日期
        if (dates.length === 2) {
            const startDate = new Date(dates[0]);
            const endDate = new Date(dates[1]);
            
            // 將信息存入結果數組
            results.push({ h3Text, startDate, endDate, hrefLink });
        }
    });

    // 根據起始日期從舊到新排序
    results.sort((a, b) => a.startDate - b.startDate);

    // 格式化日期為 YYYY/MM/DD 的形式
    function formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0'); // 月份從 0 開始，所以要加 1
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}/${month}/${day}`;
    }

    // 輸出結果
    results.forEach(result => {
        const output = `${result.h3Text};${formatDate(result.startDate)};${formatDate(result.endDate)};${result.hrefLink}`;
        console.log(output);
    });
}

// 調用函數以執行提取和排序操作
extractAndSortElements();
