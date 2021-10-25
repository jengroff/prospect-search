describe('Prospect Search', function () {
  it('Displays the home page.', function () {
    cy.visit('/');
    cy.get('h1').should('contain', 'Prospect Search');
  });
});