import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { vi } from 'vitest';
import SearchScreen from '../../pages/SearchScreen';
import { database } from '../../api';

vi.mock('../../api', () => ({
  database: {
    select: vi.fn(),
  },
}));

describe('SearchScreen', () => {
  it('loads plants from the API and renders the list', async () => {
    vi.mocked(database.select).mockResolvedValue({
      data: [
        {
          id: 'plant-1',
          common_name: 'Samambaia',
          scientific_name: 'Nephrolepis exaltata',
          image_data: '',
          city: 'Curitiba',
          created_at: '2026-03-29T10:00:00.000Z',
        },
        {
          id: 'plant-2',
          common_name: 'Orquidea',
          scientific_name: 'Orchidaceae',
          image_data: '',
          city: 'Sao Paulo',
          created_at: '2026-03-30T10:00:00.000Z',
        },
      ],
      error: null,
    });

    render(
      <MemoryRouter>
        <SearchScreen />
      </MemoryRouter>,
    );

    expect(screen.getByText('Explorar Plantas')).toBeInTheDocument();
    expect(await screen.findByText('Orquidea')).toBeInTheDocument();
    expect(screen.getByText('Samambaia')).toBeInTheDocument();
    expect(database.select).toHaveBeenCalledWith('plants');
  });
});
