from playwright.sync_api import expect

def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    toolbar_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(toolbar_title).to_be_visible()
    expect(toolbar_title).to_have_text('Courses')

    folder_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(folder_icon).to_be_visible()

    svg_path = page.get_by_test_id("courses-list-empty-view-icon").locator('path')
    expect(svg_path).to_have_attribute(
        'd',
        'M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2m0 12H4V8h16z'
    )

    view_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(view_title).to_be_visible()
    expect(view_title).to_have_text('There is no results')

    view_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(view_description).to_be_visible()
    expect(view_description).to_have_text('Results from the load test pipeline will be displayed here')



